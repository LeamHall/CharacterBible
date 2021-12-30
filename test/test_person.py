#!/usr/bin/env python3

# name:     test_person.py
# version:  0.0.3
# date:     20211230
# author:   Leam Hall
# desc:     Testing Base Person object.

import pytest
from person import Person

def test_creation(person):
  assert isinstance(person, Person)

def test_creation_full_data():
  wilbur = Person(first_name = "Wilbur", last_name = "Lefron")
  assert wilbur.get_attr('first_name') == 'Wilbur'

def test_set_attr_string(person):
  person.set_attr('middle_name', 'Ester')
  expected_attr = 'Ester'
  assert person.get_attr('middle_name') == expected_attr

def test_get_attr_fail(person):
  fail = person.get_attr('kissing habits')
  assert fail == None

 
