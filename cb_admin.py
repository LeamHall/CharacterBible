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

from datamine import datamine
from person import person_builder

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-b", "--backup", help = "-b", action='store_true')
arg_parser.add_argument("-i", "--input", help = "-i <line|of|csv||data>", type = str)
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
elif args.input:
  input_list            = args.input.split('|')
  data                  = {}
  data['table']         = 'people'
  data['last_name']     = input_list[0] or 'NULL'
  data['first_name']    = input_list[1] or 'NULL' 
  data['middle_name']   = input_list[2] or 'NULL'
  data['gender']        = input_list[3] or 'NULL'
  data['birthdate']     = input_list[4] or 'NULL'
  data['plot']          = input_list[5] or 'NULL'
  data['temperament']   = input_list[6] or 'NULL'
  data['notes']         = input_list[7] or 'NULL'
  dm.insert(data)
  
  

