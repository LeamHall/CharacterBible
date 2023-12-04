from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess

app = FastAPI()

body = (
    "<html>"
    "<body><h2>Look for people</h2>"
    "<a href='/people'>Get everyone</a>"
    "</body></html>"
)

form = """
  <form action="http://0.0.0.0:8000/people" method="GET">
  <input type="submit">
  </form>
  """

rundir = "/app/"
datadir = "/data/"
cmd_str = f"{rundir}character_bible.py"
options = ["-D", datadir, "-o", "html"]
cmd = [cmd_str]
cmd = cmd + options


@app.get("/people/{idx}", response_class=HTMLResponse)
async def get_people(idx: str):
    idx_cmd = cmd + ["-I", idx]
    query_result = subprocess.run(idx_cmd, capture_output=True)
    query_data = query_result.stdout.decode("utf-8")
    query_data = query_data.replace("\n", "")
    html_response = f"<html><body></p>{query_data}</body></html>"
    return HTMLResponse(content=html_response, status_code=200)


@app.get("/people", response_class=HTMLResponse)
async def get_people():
    query_result = subprocess.run(cmd, capture_output=True)
    query_data = query_result.stdout.decode("utf-8")
    query_data = query_data.replace("\n", "")
    html_response = f"<html><body></p>{query_data}</body></html>"
    return HTMLResponse(content=html_response, status_code=200)


@app.get("/")
async def index():
    return HTMLResponse(content=body)
