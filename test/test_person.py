#!/usr/bin/env python3

# name:     test_person.py
# version:  0.0.2
# date:     20211225
# author:   Leam Hall
# desc:     Testing Base Person object.

import pytest
from person import Person

def test_creation(person):
  assert isinstance(person, Person)

def test_creation_full_data():
  wilbur = Person(first_name = "Wilbur", last_name = "Lefron", 
    physical = ['Wavy black hair', 'Pale skin'], mental = { 'plot': 'Save the Princess'} )
  assert wilbur.get_attr('first_name') == 'Wilbur'

def test_set_attr_string(person):
  person.set_attr('middle_name', 'Ester')
  expected_attr = 'Ester'
  assert person.get_attr('middle_name') == expected_attr

def test_set_attr_list(person):
  person.set_attr('physical', 'Short blond hair')
  person.set_attr('physical', 'Scar over right eyebrow')
  expected_attr_0 = 'Short blond hair'
  expected_attr_1 = 'Scar over right eyebrow'
  physical = getattr(person, 'physical')
  assert physical[-1] == expected_attr_1
  assert physical[-2] == expected_attr_0

def test_set_attr_dict(person):
  k = 'plot'
  person.set_attr('mental', 'fight great evil', k)
  expected_attr = 'fight great evil'
  mental = getattr(person, 'mental')
  assert mental[k] == expected_attr

def test_get_attr_fail(person):
  fail = person.get_attr('kissing habits')
  assert fail == None
 
