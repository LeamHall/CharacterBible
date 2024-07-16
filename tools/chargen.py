#!/usr/bin/env python

# name    :  chargen.py
# version :  0.0.1
# date    :  20240715
# author  :  Leam Hall
# desc    :  Create characters

"""
Create a character.
"""

import random
import sqlite3

DB = "data/chargen.db"


def get_first_name(gender, db):
    """Return a random first name based on gender, if none given."""
    return "Alba"


def get_last_name(cur):
    """Return a random last name if none given."""
    command = "SELECT name FROM last_name LIMIT 1"
    result = cur.execute(command)
    name = result.fetchone()[0]
    return name


def get_gender(gender):
    """Return a random gender if none given."""
    if not gender:
        gender = random.choice(["m", "f"])
    return gender


def build_character(database, gender=None):
    """Build the character data structure."""
    con = sqlite3.connect(database)
    cur = con.cursor()

    gender = get_gender(gender)
    c = {
        "first_name": get_first_name(gender, None),
        "last_name": get_last_name(cur),
        "gender": gender,
    }

    return c


if __name__ == "__main__":
    db = DB

    character = build_character(db, gender=None)
