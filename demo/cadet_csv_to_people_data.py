#!/usr/bin/env python

# name:     cadet_csv_to_people_data.py
# version:  0.0.1
# date:     20211228
# author:   Leam Hall
# desc:     Pull cadet csv into format for people.db


datafile  = 'data/firster_academy_cadets_1429_update.csv'
sqlfile   = 'data/add_people_data.sql'

with open(sqlfile, 'w') as output:
  output.write( "-- name:    add_people_data.sql \n")
  output.write( "-- version: 0.0.1\n")
  output.write( "-- date:    20211228\n")
  output.write( "-- author:  Leam Hall\n")
  output.write( "-- desc:    Populate people stuff database.\n")
  output.write( "\n")
  output.write( "BEGIN DEFERRED;\n")
  output.write( "\n")

  with open(datafile, 'r') as data:
    for line in data.readlines():
      line = line.strip()
      _id, last_name, first_name, gender, upp, b_year, b_day, notes =  line.split(':')
      birthdate = str(b_year) + str(b_day)
      birthdate = int(birthdate) 
      if not notes:
        notes = 'NULL'
      formatted = ( f'INSERT INTO people ( last_name, first_name, middle_name, ' 
        f'suffix_name, other_name, gender, birthdate, plot, temperament, notes) '
        f'VALUES ( "{last_name}", "{first_name}", NULL, NULL, NULL, '
        f'"{gender.lower()}", {birthdate}, NULL, NULL, "{notes}" ); '
        f"\n"
      )
      output.write(formatted)

  output.write( "\n")
  output.write("END;\n")
  output.write( "\n")

