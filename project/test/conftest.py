# name:     conftest.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Shared data for tests.

import pytest
import os
import sqlite3

from app.person import Person
from app.person import Character
from app.person.person_builder import PersonBuilder
from app.person.character_builder import CharacterBuilder
from app.datamine import datamine

@pytest.fixture()
def db():
  con  = sqlite3.connect(":memory:")
  cur  = con.cursor()

  all_files = os.listdir('database') 
  for file in all_files:
    if file.startswith("write_"):
      filename = os.path.join('database', file)
      with open(filename, 'r') as f:
        sqlcmd = f.read()
        con.executescript(sqlcmd)
  for file in all_files:
    if file.startswith("test_add_"):
      filename = os.path.join('database', file)
      with open(filename, 'r') as f:
          sqlcmd = f.read()
          con.executescript(sqlcmd)
  return cur
 
@pytest.fixture()
def person():
  p   = Person( idx = 123, first_name = "Alba", last_name = "Domici", 
        birthdate = 1416146, gender = "f",  notes = 'Trail Rat')
  return p 

@pytest.fixture()
def character():
  p       = Person( idx = 123, first_name = "Alba", last_name = "Domici", 
            birthdate = 1416146, gender = "f",  notes = 'Trail Rat')
  stats   = { 'str': 7, 'dex': 8, 'end':10, 'int':6, 'edu':7, 'soc': 12 } 
  skills  = { "GunCbt(CbtR)": 2, "Math": 0, "Kissing": 2 }
  data    = { 'person':p, 'stats': stats, 'skills':skills }
  c       = Character(**data)
  return c

@pytest.fixture()
def amanda():
  p       = Person( first_name = "Amanda", last_name = "Lefron", 
            birthdate = 1432150, gender = "f")
  stats   = { 'str': 2, 'dex': 2, 'end':6, 'int':2, 'edu':2, 'soc': 12 } 
  skills  = { "GunCbt(CbtR)": 2, "Math": 0, "Kissing": 2 }
  data  = { 'person':p, 'skills': skills,  'stats' : stats}
  cb    = CharacterBuilder(data)
  a     = cb.return_character()
  return a

@pytest.fixture()
def cb():
  p       = Person( first_name = "Amanda", last_name = "Lefron", 
            birthdate = 1432150, gender = "f")
  stats   = { 'str': 2, 'dex': 2, 'end':6, 'int':2, 'edu':2, 'soc': 12 } 
  skills  = { "GunCbt(CbtR)": 2, "Math": 0, "Kissing": 2 }
  data    = { 'person':p, 'skills': skills,  'stats' : stats}
  cb      = CharacterBuilder(data)
  return cb

@pytest.fixture()
def pb():
  pb = PersonBuilder()
  return pb          

@pytest.fixture()
def person_base():
  pb = PersonBuilder()
  person_base = pb.set_data()
  return person_base

@pytest.fixture()
def dm():
  dm = datamine.Datamine(":memory:")
  dm.build_test_db(":memory:")
  return dm
