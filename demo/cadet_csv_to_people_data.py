#!/usr/bin/env python

# name:     cadet_csv_to_people_data.py
# version:  0.0.1
# date:     20211228
# author:   Leam Hall
# desc:     Pull cadet csv into people db


import sqlite3

datafile  = 'data/firster_academy_cadets_1429_update.csv'
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
    _id, last_name, first_name, gender, upp, b_year, b_day, notes =  line.split(':')
    birthdate = str(b_year) + str(b_day)
    birthdate = int(birthdate) 
    data  = {}
    data['last_name']   = last_name
    data['first_name']  = first_name
    data['gender']      = gender.lower()    
    data['birthdate']   = birthdate
    data['notes']       = notes
    cur.execute(query, data)
    con.commit()

con.close()

