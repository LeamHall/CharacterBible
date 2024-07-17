#!/usr/bin/env python

# name    :  test/test_chargen.py
# version :  0.0.1
# date    :  20240715
# author  :  Leam hall
# desc    :  Tests for chargen.py

"""
Testing the chargen.py tool.
"""

import sqlite3
import unittest

import chargen as c


class TestChargen(unittest.TestCase):
    """
    Testing the chargen.py tool.
    """

    def setUp(self):
        self.db = "test/data/chargen.db"
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()

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
        character = c.build_character(self.db, gender)
        self.assertIsInstance(character, dict)
        self.assertEqual(character["first_name"], "Alba")
        self.assertEqual(character["last_name"], "Lefron")
        self.assertEqual(character["gender"], "f")

    def test_build_male_character(self):
        gender = "m"
        character = c.build_character(self.db, gender)
        self.assertIsInstance(character, dict)
        self.assertEqual(character["first_name"], "Wilbur")
        self.assertEqual(character["last_name"], "Lefron")
        self.assertEqual(character["gender"], "m")
