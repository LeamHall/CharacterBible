# name:     test_person_builder.py
# version:  0.0.1
# date:     20211225
# author:   Leam Hall
# desc:     test person_builder

import pytest

from person import Person
from person.person_builder import PersonBuilder

def test_create_basic():
  b = Person()
  pb  = PersonBuilder()
  p   = pb.gen_data(b)
  assert isinstance(p, Person)

def test_basic_person():
  boy         = Person()
  pb          = PersonBuilder()
  b = pb.gen_data(boy)
  assert isinstance(b, Person)
  assert b.first_name     == 'John'
  assert b.last_name      == 'Dough'
  assert b.gender         == 'm'
  assert b.birth_info     == { 'year': 1234, 'day': 56 }
  assert b.notes          == ''

def test_generated_person():
  girl  = Person()
  data  = { 'first_name' : 'Jane', 'last_name' : 'Dont', 'gender' : 'f', 
          'birth_info' : { 'year': 1236, 'day': 56 }, 'notes' : 'calm' }
  pb    = PersonBuilder()
  g     = pb.gen_data(girl, data)
  assert g.first_name     == 'Jane'
  assert g.last_name      == 'Dont'
  assert g.gender         == 'f'
  assert g.birth_info     == { 'day': 56, 'year': 1236 }
  assert g.notes          == 'calm'

def test_existing_person_data():
  girl  = Person()
  data  = { 'first_name': 'Susie', 'last_name': 'Dont', '_id': 867 }
  pb    = PersonBuilder()
  g     = pb.set_data(girl, data)
