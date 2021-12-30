#!/usr/bin/env python

# name:     person.py
# version:  0.0.1
# date:     20211229
# author:   Leam Hall
# desc:     CRUD Person with DB.

import argparse

from datamine import datamine
from person import person
from view import person as person_view
from person import person_builder

parser    = argparse.ArgumentParser("Create, Review, Update, or Delete a person.")
parser.add_argument("-i", "--idx", help = "-i <IDX>", type = int)
parser.add_argument("-c", "--column", help = "-c 'last_name'", type = str)
parser.add_argument("-l", "--like", help = "-l 'Lefron'", type = str)
parser.add_argument("-o", "--output", help = "-o <text|html>", type = str, default = 'text')
args = parser.parse_args()

dm        = datamine.Datamine('data/people.db')
pb        = person_builder.PersonBuilder()

criteria  = {'table': 'people'}

def result_to_buildable(result):
  ''' Take a data result and return a person object '''
  data_keys = ['idx', 'last_name', 'first_name', 'middle_name',
    'gender', 'birthdate', 'plot', 'temperament', 'notes' ]
  data = {}
  for idx, key in enumerate(data_keys):
    data[key] = result[idx]
  p = person.Person()
  P = pb.set_data(p, data)
  print(P)
  return P 
  
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

