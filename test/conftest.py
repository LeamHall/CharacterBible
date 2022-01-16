# name:     conftest.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Shared data for tests.

import pytest
from person import Person
from person.person_builder import PersonBuilder
from datamine import datamine

@pytest.fixture()
def person():
  p   = Person( idx = 123, first_name = "Alba", last_name = "Domici", 
        birthdate = 1416146, gender = "f",  notes = 'Trail Rat')
  return p 

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
  #dm = datamine.Datamine('data/people.db')
  dm = datamine.Datamine(":memory:")
  dm.build_test_db(":memory:")
  return dm
