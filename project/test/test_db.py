#!/usr/bin/env python

import os
import unittest
import sqlite3

class DBTestCase(unittest.TestCase):
  def setUp(self):
    self.con  = sqlite3.connect(":memory:")
    self.cur  = self.con.cursor()

    all_files = os.listdir('database') 
    for file in all_files:
      if file.startswith("write_"):
        filename = os.path.join('database', file)
        with open(filename, 'r') as f:
          sqlcmd = f.read()
          self.con.executescript(sqlcmd)
    for file in all_files:
      if file.startswith("test_add_"):
        filename = os.path.join('database', file)
        with open(filename, 'r') as f:
          sqlcmd = f.read()
          self.con.executescript(sqlcmd)

  def tearDown(self):
    self.con.close()

  def test_db_name_count(self):
    stmt = "SELECT COUNT(*) FROM people"
    self.cur.execute(stmt)
    result = self.cur.fetchone()[0]
    self.assertEqual(result, 1, "found 1 row") 

  def test_db_last_name(self):
    stmt = "SELECT last_name FROM people LIMIT(1)"
    self.cur.execute(stmt)
    result = self.cur.fetchone()[0]
    self.assertEqual(result, 'Romero', "Found the right last name")

if __name__ == '__main__':
  unittest.main()
