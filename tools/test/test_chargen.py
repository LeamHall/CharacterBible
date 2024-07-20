#!/usr/bin/env python

# name    :  test/test_chargen.py
# version :  0.0.1
# date    :  20240715
# author  :  Leam hall
# desc    :  Tests for chargen.py

"""
Testing the chargen.py tool.
"""

import argparse
import os.path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

import tools.chargen as c


class TestChargen(unittest.TestCase):
    """
    Testing the chargen.py tool.
    """

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()  # pylint: disable=R1732
        self.db = os.path.join(self.test_dir.name, "test_chargen.db")
        self.con = sqlite3.connect(self.db)
        with self.con:
            self.cur = self.con.cursor()
            create_commands = [
                "CREATE TABLE plots (plot  TEXT);",
                "CREATE TABLE temperaments (temperament);",
                "CREATE TABLE male_first_name ( name varchar[20] UNIQUE);",
                "CREATE TABLE female_first_name ( name varchar[20] UNIQUE);",
                "CREATE TABLE last_name ( name varchar[20] UNIQUE);",
            ]
            for command in create_commands:
                self.cur.execute(command)
            self.con.commit()
            insert_commands = [
                "INSERT INTO plots VALUES ('trauma');",
                "INSERT INTO temperaments VALUES ('Teacher');",
                "INSERT INTO last_name VALUES ('Lefron');",
                "INSERT INTO female_first_name VALUES ('Alba');",
                "INSERT INTO male_first_name VALUES ('Wilbur');",
            ]
            for command in insert_commands:
                self.cur.execute(command)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_get_item(self):
        command = "SELECT name FROM last_name ORDER BY RANDOM() LIMIT 1"
        expected = "Lefron"
        result = c.get_item(self.cur, command)
        self.assertEqual(expected, result)

    def test_get_gender(self):
        for _ in range(0, 10):
            gender = None
            expected = ["f", "m"]
            result = c.get_gender(gender)
            self.assertTrue(result in expected)

    def test_build_female_character(self):
        gender = "f"
        cur = c.get_cursor(self.db)
        character = c.build_character(cur, gender)
        self.assertIsInstance(character, dict)
        self.assertEqual(character["first_name"], "Alba")
        self.assertEqual(character["last_name"], "Lefron")
        self.assertEqual(character["gender"], "f")
        self.assertEqual(character["plot"], "trauma")
        self.assertEqual(character["temperament"], "Teacher")

    def test_build_male_character(self):
        gender = "m"
        cur = c.get_cursor(self.db)
        character = c.build_character(cur, gender)
        self.assertIsInstance(character, dict)
        self.assertEqual(character["first_name"], "Wilbur")
        self.assertEqual(character["last_name"], "Lefron")
        self.assertEqual(character["gender"], "m")
        self.assertEqual(character["plot"], "trauma")
        self.assertEqual(character["temperament"], "Teacher")

    def test_get_cursor(self):
        result = c.get_cursor(self.db)
        self.assertIsInstance(result, sqlite3.Cursor)

    def test_parse_args(self):
        testargs = ["chargen.py", "-d", self.db, "-n", "5"]
        with patch.object(sys, "argv", testargs):
            result = c.parse_args()
            self.assertIsInstance(result, argparse.Namespace)
            self.assertEqual(result.database, self.db)
            self.assertEqual(result.number, 5)
