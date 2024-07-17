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


def get_item(cur, command):
    result = cur.execute(command)
    item = result.fetchone()[0]
    return item


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
    if gender == "f":
        f_name_cmd = (
            "SELECT name FROM female_first_name ORDER BY RANDOM() LIMIT 1;"
        )
    else:
        f_name_cmd = (
            "SELECT name FROM male_first_name ORDER BY RANDOM() LIMIT 1;"
        )

    l_name_cmd = "SELECT name FROM last_name ORDER BY RANDOM() LIMIT 1;"
    c = {
        "first_name": get_item(cur, f_name_cmd),
        "last_name": get_item(cur, l_name_cmd),
        "gender": gender,
    }

    cur.close()
    return c


if __name__ == "__main__":
    character = build_character(DB, gender=None)
    print(character)
