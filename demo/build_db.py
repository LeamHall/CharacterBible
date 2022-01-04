import sqlite3
import os

con = sqlite3.connect("data/toy_people.db")
cur = con.cursor()
start_dir = os.getcwd()

files = os.listdir('database')
os.chdir('database')
for file in files:
  if file.startswith('write_'):
    print(f"file is {file}")
    with open(file, 'r') as f:
      sqlcmd = f.read()
      cur.executescript(sqlcmd)

for file in files:
  if file.startswith('test_add_'):
    print(f"file is {file}")
    with open(file, 'r') as f:
      sqlcmd = f.read()
      cur.executescript(sqlcmd)

cur.close()
con.close()

