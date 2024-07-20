#!/usr/bin/env python

# name:     add_people_sample.py
# version:  0.0.1
# date:     20211230
# author:   Leam Hall
# desc:     Pull sample people csv into people db


import sqlite3

DATAFILE = "data/sample_people.csv"
DB = "data/people.db"
CON = sqlite3.connect(DB)
CUR = CON.cursor()

# schema and populate people from csv.
QUERY = """INSERT INTO people (last_name, first_name, gender, birthdate, notes)
              VALUES ( :last_name, :first_name, :gender, :birthdate, :notes)"""

CON.commit()

with open(DATAFILE, "r") as data:
    for line in data.readlines():
        line = line.strip()
        (
            idx,
            last_name,
            first_name,
            middle_name,
            gender,
            birthdate,
            plot,
            temperament,
            notes,
        ) = line.split("|")
        data = {}
        data["last_name"] = last_name
        data["first_name"] = first_name
        data["middle_name"] = middle_name
        data["gender"] = gender
        data["birthdate"] = birthdate
        data["plot"] = plot
        data["temperament"] = temperament
        data["notes"] = notes
        CUR.execute(QUERY, data)
        CON.commit()

CON.close()
