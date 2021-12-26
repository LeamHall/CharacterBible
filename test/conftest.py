# name:     conftest.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Shared data for tests.

import pytest
from person import Person
from person.person_builder import PersonBuilder

@pytest.fixture()
def person():
  p   = Person( first_name = "Alba", last_name = "Domici", gender = "f",
        physical = ["raging blue eyes"],
        mental = { "temperament": 'gung-ho' })
  return p 

@pytest.fixture()
def pb():
  pb = PersonBuilder()
  return pb          

@pytest.fixture()
def person_base():
  pb = PersonBuilder()
  person_base = pb.return_person()
  return person_base

