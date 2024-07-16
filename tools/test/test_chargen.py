#!/usr/bin/env python

# name    :  test/test_chargen.py
# version :  0.0.1
# date    :  20240715
# author  :  Leam hall
# desc    :  Tests for chargen.py

"""
Testing the chargen.py tool.
"""

import random
import sqlite3
import unittest

import chargen as c


class TestChargen(unittest.TestCase):
    """
    Testing the chargen.py tool.
    """

    def setUp(self):
        self.result = {"first_name": "Alba", "last_name": "Lefron"}
        self.db = "test/data/chargen.db"
        self.con = sqlite3.connect(self.db)
        self.cur = self.con.cursor()

    def test_basic_data(self):
        expected = {"first_name": "Alba", "last_name": "Lefron"}
        self.assertEqual(self.result, expected)

    def test_get_first_name(self):
        gender = None
        db = None
        expected = "Alba"
        result = c.get_first_name(gender, db)
        self.assertEqual(expected, result)

    def test_get_last_name(self):
        expected = "Lefron"
        result = c.get_last_name(self.cur)
        self.assertEqual(expected, result)

    def test_get_gender(self):
        for _ in range(0, 10):
            gender = None
            expected = ["f", "m"]
            result = c.get_gender(gender)
            self.assertTrue(result in expected)

        for _ in range(0, 10):
            gender = random.choice(["m", "f", "n"])
            expected = gender
            result = c.get_gender(gender)
            self.assertEqual(expected, result)

    def test_build_character(self):
        db = None
        gender = "f"
        db = self.db
        character = c.build_character(db, gender)
        self.assertIsInstance(character, dict)
        self.assertEqual(character["first_name"], "Alba")
        self.assertEqual(character["last_name"], "Lefron")
        self.assertEqual(character["gender"], "f")
