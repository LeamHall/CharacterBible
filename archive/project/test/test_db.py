#!/usr/bin/env python

import os
import pytest
import sqlite3

def test_db_name_count(db):
  stmt = "SELECT COUNT(*) FROM people"
  db.execute(stmt)
  result = db.fetchone()[0]
  assert(result == 3)

def test_db_last_name(db):
  stmt = "SELECT last_name FROM people LIMIT(1)"
  db.execute(stmt)
  result = db.fetchone()[0]
  assert(result == 'Romero')

def test_db_skill_levels(db):
  stmt = """select p.first_name, p.last_name,
  (SELECT sl.skill FROM skills sl WHERE psl.skill_idx = sl.idx) as skill_name,
  psl.skill_level
  from people p left outer join people_skill_level psl on p.idx = psl.people_idx;"""

  db.execute(stmt)
  result = db.fetchall()[2]
  assert(result == ('Jakob', 'Domici', 'Kissing', 1))

