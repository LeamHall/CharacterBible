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

defaults  = { 'config':'sample.cfg', 'section':'default'}
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-c", "--column", type = str)
arg_parser.add_argument("-C", "--config", type = str, default = "sample.cfg")
arg_parser.add_argument("-d", "--db", type = str)
arg_parser.add_argument("-D", "--datadir", type = str)
arg_parser.add_argument("-i", "--idx", type = int)
arg_parser.add_argument("-l", "--like", type = str)
arg_parser.add_argument("-o", "--output", help = "<csv|text|html>", 
  type = str, default = 'text')
arg_parser.add_argument("-S", "--section", type = str, default = 'default')
args = arg_parser.parse_args()

config_parser = ConfigParser()
config_parser.read(args.config)
config    = {}
criteria  = {}
for name, value in config_parser.items(args.section):
  config[name] = config_parser[args.section][name]

defaults.update(config)
defaults.update(vars(args))
criteria['table'] = defaults['table']

try:
  database  = os.path.join( config['datadir'], config['db'] )
  dm        = datamine.Datamine(database)
  pb        = person_builder.PersonBuilder()
except Exception as e:
  print(e)
  

def get_single_value(idx, table):
  criteria  = { 'idx': idx, 'table': table }
  result    = dm.get_by_idx(criteria)
  return    result[0][1]

def result_to_buildable(result):
  ''' Take a data result and return a person object '''
  data_keys = ['idx', 'last_name', 'first_name', 'middle_name',
    'gender', 'birthdate', 'plot', 'temperament', 'notes' ]
  data = {}
  for idx, key in enumerate(data_keys):
    data[key] = result[idx]
  if data['plot']:
    data['plot']  = get_single_value(data['plot'], 'plots')
  if data['temperament']:
    data['temperament'] = get_single_value(data['temperament'], 'temperaments')
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

