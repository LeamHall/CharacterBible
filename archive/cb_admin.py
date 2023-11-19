#!/usr/bin/env python

# name:     cb_admin.py
# version:  0.0.2
# date:     20220115
# author:   Leam Hall
# desc:     Administrative functions for the CharacterBible

import argparse
from configparser import ConfigParser
import copy
from datetime import date
import os
import sqlite3
import sys

from datamine import datamine
from person import person_builder


###
def csv_to_dict(data, line, sep="|"):
    """Breaks a CSV line into key, value pairs, returns dict of d[k] = v
    Sample line:
    "last_name=Domici|first_name=Al|middle_name=Ester|gender=f"
    """
    updated = copy.deepcopy(data)
    for phrase in line.split(sep):
        key, value = phrase.split("=")
        updated[key] = value
    return updated


def kv_to_dict(data, line):
    """Breaks a key=value string into key and value"""
    updated = copy.deepcopy(data)
    key, value = line.split("=")
    updated["column"] = key
    updated["value"] = value
    return updated


def sort_args(defaults, config, args):
    """Returns dict of configuration, with defaults lowest priority,
    then config file options, then CLI args as highest.
    """
    defaults = copy.deepcopy(defaults)
    defaults.update(config)
    for key, value in vars(args).items():
        if value is not None:
            defaults[key] = value
    return defaults


###

defaults = {"section": "default", "config": "sample.cfg"}
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-b", "--backup", action="store_true")
arg_parser.add_argument("-C", "--config", default="sample.cfg")
arg_parser.add_argument(
    "-i", "--input", help="-i <last_name=Smith|first_name=Janie>"
)
arg_parser.add_argument("-I", "--idx", type=int)
arg_parser.add_argument("-k", "--keys", action="store_true")
arg_parser.add_argument("-r", "--remove", type=int)
arg_parser.add_argument("-S", "--section", default="default")
arg_parser.add_argument("-t", "--table")
arg_parser.add_argument("-u", "--update", help="<column>=<value>")
args = arg_parser.parse_args()

today = date.today().strftime("%Y%m%d")
config_parser = ConfigParser()
config_parser.read(args.config)
config = {}
section = args.section
for name, value in config_parser.items(section):
    config[name] = config_parser[section][name]

defaults = sort_args(defaults, config, args)

try:
    database = os.path.join(defaults["datadir"], defaults["db"])
    if not os.path.exists(database):
        raise FileNotFoundError
    dm = datamine.Datamine(database)
    pb = person_builder.PersonBuilder()
except FileNotFoundError:
    print(f"Database {database} does not exist")
    sys.exit()


if args.backup:
    backup_database_name = f"backup_{today}_{config['db']}"
    backup_database = os.path.join(defaults["datadir"], backup_database_name)

    con = sqlite3.connect(database)
    bck = sqlite3.connect(backup_database)
    with bck:
        con.backup(bck, pages=0)
    bck.close()
    con.close()
elif args.keys:
    data = {}
    data["table"] = defaults["table"]
    keys = ", ".join(dm.keys(data))
    print(keys)
elif args.remove:
    data = {}
    data["table"] = defaults["table"]
    data["idx"] = args.remove
    dm.remove_by_idx(data)
elif args.input:
    data = {}
    data["table"] = defaults["table"]
    data = csv_to_dict(data, args.input)
    dm.insert(data)
elif args.update:
    data = {}
    data["table"] = defaults["table"]
    data["idx"] = defaults["idx"]
    data = kv_to_dict(data, args.update)
    dm.update_by_idx_column(data)
