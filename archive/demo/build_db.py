#!/usr/bin/env python

# name:     build_db.py
# version:  0.0.1
# date:     20220108
# author:   Leam Hall
# desc:     Build and populate the database.

import argparse
from configparser import ConfigParser
import sqlite3
import os

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-d", "--db", type=str)
arg_parser.add_argument("-D", "--datadir", type=str)
arg_parser.add_argument(
    "-t", "--test", help="Load test data", action="store_true"
)
args = arg_parser.parse_args()

config_parser = ConfigParser()
config_parser.read("sample.cfg")
config = {}
config["test"] = False
for name, value in config_parser.items("default"):
    config[name] = config_parser["default"][name]

if args.datadir:
    config["datadir"] = args.datadir
if args.db:
    config["db"] = args.db
if args.test:
    config["test"] = args.test

try:
    database = os.path.join(config["datadir"], config["db"])
    con = sqlite3.connect(database)
    cur = con.cursor()
except Exception as e:
    print(e)
    os.exit()

start_dir = os.getcwd()
all_files = os.listdir("database")
build_files = []
add_files = []
os.chdir("database")
for file in all_files:
    if file.startswith("write_"):
        build_files.append(file)
    if config["test"] and file.startswith("test_add_"):
        add_files.append(file)
    elif not config["test"] and file.startswith("add_"):
        add_files.append(file)

for file in build_files + add_files:
    with open(file, "r") as f:
        sqlcmd = f.read()
        cur.executescript(sqlcmd)

cur.close()
con.close()
os.chdir(start_dir)
