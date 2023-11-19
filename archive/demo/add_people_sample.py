#!/usr/bin/env python

# name:     add_people_sample.py
# version:  0.0.1
# date:     20211230
# author:   Leam Hall
# desc:     Pull sample people csv into people db


import sqlite3

datafile  = 'data/sample_people.csv'
db        = 'data/people.db'
con       = sqlite3.connect(db)
cur       = con.cursor()

# schema and populate people from csv.
query     = """INSERT INTO people (last_name, first_name, gender, birthdate, notes ) 
              VALUES ( :last_name, :first_name, :gender, :birthdate, :notes )"""

con.commit()

with open(datafile, 'r') as data:
  for line in data.readlines():
    line = line.strip()
    idx, last_name, first_name, middle_name, gender, birthdate, plot, temperament, notes =  line.split('|')
    data  = {}
    data['last_name']   = last_name
    data['first_name']  = first_name
    data['middle_name'] = middle_name
    data['gender']      = gender
    data['birthdate']   = birthdate
    data['plot']        = plot
    data['temperament'] = temperament
    data['notes']       = notes
    cur.execute(query, data)
    con.commit()

con.close()

