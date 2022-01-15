#!/usr/bin/env python

# name:     cb_admin.py
# version:  0.0.2
# date:     20220115
# author:   Leam Hall
# desc:     Administrative functions for the CharacterBible

import argparse
from configparser import ConfigParser
from datetime import date
import os
import sqlite3

import copy

from datamine import datamine
from person import person_builder

###
def csv_to_dict(data, line, sep='|'):
  """ Breaks a CSV line into key, value pairs, returns dict of d[k] = v 
      Sample line:
      "last_name=Domici|first_name=Al|middle_name=Ester|gender=f"
  """
  updated = copy.deepcopy(data)  
  for phrase in line.split(sep):
    key, value = phrase.split("=")
    updated[key] = value
  return updated

###
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-b", "--backup", help = "-b", action = 'store_true')
arg_parser.add_argument("-i", "--input", help = "-i <line|of|csv||data>", type = str)
arg_parser.add_argument("-k", "--keys", action = 'store_true')
arg_parser.add_argument("-t", "--table", type = str)
args = arg_parser.parse_args()

today = date.today().strftime('%Y%m%d')
config_parser = ConfigParser()
config_parser.read('sample.cfg')
config = {}
section = 'default'
for name, value in config_parser.items(section):
  config[name] = config_parser[section][name]

try:
  database  = os.path.join( config['datadir'], config['db'] )
  dm        = datamine.Datamine(database)
  pb        = person_builder.PersonBuilder()
except Exception as e:
  print(e)


if args.backup:
  backup_database_name = f"backup_{today}_{config['db']}"
  backup_database = os.path.join( config['datadir'], backup_database_name )

  con = sqlite3.connect(database)
  bck = sqlite3.connect(backup_database)
  with bck:
    con.backup(bck, pages=0)
  bck.close()
  con.close()
elif args.keys:
  data                  = {}
  data['table']         = args.table
  keys                  = ', '.join(dm.keys(data))
  print(keys)
elif args.input:
  data                  = {}
  data['table']         = args.table
  data = csv_to_dict(data, args.input)
  dm.insert(data)
  
  

