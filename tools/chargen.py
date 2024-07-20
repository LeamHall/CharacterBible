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


def roll_d6(count):
    """Return a total of 'count' instances of 1 to 6."""
    total = 0
    for _ in range(count):
        total += random.randint(1, 6)
    return total


def roll_modified_d6(base_roll):
    """Return a d6 roll modified by how high or low the base_roll is."""
    return base_roll + random.randint(1, 3) + random.randint(1, 3)


def stat_modifier(base_roll, num_dice):
    """Return a stat modifier based on a 3d6 stat."""
    modifier = 0
    if num_dice == 3:
        if base_roll == 18:
            modifier = "+3"
        elif base_roll in range(15, 18):
            modifier = "+2"
        elif base_roll in range(12, 15):
            modifier = "+1"
        elif base_roll == 3:
            modifier = "-3"
        elif base_roll in range(4, 8):
            modifier = "-2"
        elif base_roll in range(8, 9):
            modifier = "-1"
    return modifier


def roll_stats():
    """Fills the stat dict with similar numbers."""
    stats = {
        "2d6": {
            "str": 0,
            "dex": 0,
            "end": 0,
            "int": 0,
            "edu": 0,
            "soc": 0,
        },
        "3d6": {
            "str": 0,
            "int": 0,
            "wis": 0,
            "dex": 0,
            "con": 0,
            "cha": 0,
        },
        "ch_bx": {
            "str": 0,
            "int": 0,
            "wis": 0,
            "dex": 0,
            "con": 0,
            "cha": 0,
        },
    }
    matches = {
        "str": "str",
        "int": "int",
        "dex": "dex",
        "end": "con",
        "edu": "wis",
        "soc": "cha",
    }

    for key in stats["2d6"].keys():
        roll = roll_d6(2)
        stats["2d6"][key] = roll
        key3 = matches[key]
        stats["3d6"][key3] = roll_modified_d6(roll)

    for key in stats["3d6"].keys():
        base_value = stats["3d6"][key]
        modifier = stat_modifier(base_value, 3)
        if modifier != 0:
            stats["ch_bx"][key] = modifier

    return stats


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
        "stats": roll_stats(),
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
