#!/usr/bin/env python

# name:     character_bible.py
# version:  0.0.2
# date:     20220101
# author:   Leam Hall
# desc:     Store, view, update, remove Person with SQLite DB.

import argparse
from configparser import ConfigParser
import os 

from datamine import datamine
from person import person
from view import person as person_view
from person import person_builder

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-c", "--column", help = "-c 'last_name'", type = str)
arg_parser.add_argument("-d", "--db", help = "-d <database>", type = str)
arg_parser.add_argument("-D", "--datadir", help = '-D <datadir>', type = str)
arg_parser.add_argument("-i", "--idx", help = "-i <IDX>", type = int)
arg_parser.add_argument("-l", "--like", help = "-l 'Lefron'", type = str)
arg_parser.add_argument("-o", "--output", help = "-o <csv|text|html>", type = str, default = 'text')
args = arg_parser.parse_args()

config_parser = ConfigParser()
config_parser.read('sample.cfg')
config    = {}
criteria  = {}
for name, value in config_parser.items('default'):
  config[name] = config_parser['default'][name]

criteria['table'] = config['table']

# command line arguments take precedence over config file settings.
if args.datadir:
  config['datadir'] = args.datadir
if args.db:
  config['db'] = args.db

try:
  database  = os.path.join( config['datadir'], config['db'] )
  dm        = datamine.Datamine(database)
  pb        = person_builder.PersonBuilder()
except Exception as e:
  print(e)
  


def result_to_buildable(result):
  ''' Take a data result and return a person object '''
  data_keys = ['idx', 'last_name', 'first_name', 'middle_name',
    'gender', 'birthdate', 'plot', 'temperament', 'notes' ]
  data = {}
  for idx, key in enumerate(data_keys):
    data[key] = result[idx]
  p = pb.set_data(person.Person(), data)
  return p 
  
def show_results(results, output_type = args.output):
  for r in results:
    P = result_to_buildable(r)
    print(person_view.char_string(P, output_type))
    if output_type == 'text':
      print("----")
    elif output_type == 'html':
      print("<p></p>")
    else:
      print("\n")

if args.idx:
  criteria['idx'] = args.idx
  results = dm.get_by_idx(criteria)
  show_results(results, output_type = args.output)
elif args.column and args.like:
  criteria['like_column']  = args.column
  criteria['like']         = args.like
  results = dm.get_with_like(criteria)
  show_results(results, output_type = args.output)
else:
  results = dm.select(criteria)
  show_results(results, output_type = args.output)

