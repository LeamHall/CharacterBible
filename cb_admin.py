#!/usr/bin/env python

# name:     cb_admin.py
# version:  0.0.1
# date:     20220102
# author:   Leam Hall
# desc:     Administrative functions for the CharacterBible

import argparse
from configparser import ConfigParser
from datetime import date
import os
import sqlite3

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-b", "--backup", help = "-b", action='store_true')
args = arg_parser.parse_args()

today = date.today().strftime('%Y%m%d')
config_parser = ConfigParser()
config_parser.read('sample.cfg')
config = {}
section = 'default'
for name, value in config_parser.items(section):
  config[name] = config_parser[section][name]

database = os.path.join( config['datadir'], config['db'] )

if args.backup:
  backup_database_name = f"backup_{today}_{config['db']}"
  backup_database = os.path.join( config['datadir'], backup_database_name )

  con = sqlite3.connect(database)
  bck = sqlite3.connect(backup_database)
  with bck:
    con.backup(bck, pages=0)
  bck.close()
  con.close()

