FROM python:3

WORKDIR /app
VOLUME /data

RUN python -m pip install --upgrade pip
COPY project/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY project/main.py .
COPY project/app .
COPY project/sample.cfg .

EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ]
