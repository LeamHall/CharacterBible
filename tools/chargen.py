#!/usr/bin/env python

# name    :  chargen.py
# version :  0.0.1
# date    :  20240715
# author  :  Leam Hall
# desc    :  Create characters

"""
Create a character.
"""

import argparse
import random
import sqlite3
import sys


def parse_args():
    """Takes the arguments and returns the final config."""
    parser = argparse.ArgumentParser(
        prog="chargen.py",
        description="Generates basic characters for games.",
        epilog="",
    )

    parser.add_argument(
        "-d", "--database", help="database filename", default="data/chargen.db"
    )
    parser.add_argument(
        "-n",
        "--number",
        help="number of characters",
        type=int,
        default=1,
    )
    return parser.parse_args()


def get_item(cursor, command):
    """Returns one item using the given command."""
    result = cursor.execute(command)
    return result.fetchone()[0]


def get_gender(gender):
    """Return a random gender if none given."""
    if not gender:
        gender = random.choice(["m", "f"])
    return gender


def get_cursor(database):
    """Establish the connection and return it."""
    con = sqlite3.connect(database)
    return con.cursor()


def build_character(cursor, gender=None):
    """Build the character data structure."""
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
    plot_cmd = "SELECT plot from plots ORDER BY RANDOM() LIMIT 1;"
    temperament_cmd = (
        "SELECT temperament from temperaments ORDER BY RANDOM() LIMIT 1;"
    )
    c = {
        "first_name": get_item(cursor, f_name_cmd),
        "last_name": get_item(cursor, l_name_cmd),
        "plot": get_item(cursor, plot_cmd),
        "temperament": get_item(cursor, temperament_cmd),
        "gender": gender,
    }

    return c


if __name__ == "__main__":
    args = parse_args()
    try:
        cur = get_cursor(args.database)
    except sqlite3.Error as e:
        print(e)
        sys.exit(1)
    else:
        for _ in range(0, args.number):
            character = build_character(cur, gender=None)
            print(character)
            print("")
    finally:
        cur.close()
