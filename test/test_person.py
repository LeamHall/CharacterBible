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

@pytest.mark.skip()
def test_creation_full_data():
  # Can add an existing person's data
  pass

def test_set_attr_string(person):
  person.set_attr('last_name', 'Lefron')
  expected_attr = 'Lefron'
  assert person.get_attr('last_name') == expected_attr

def test_set_attr_list(person):
  person.set_attr('physical', 'Short blond hair')
  expected_attr = 'Short blond hair'
  physical = person.get_attr('physical')
  assert physical[0] == expected_attr

@pytest.mark.skip()
def test_get_attr(self):
  # Graceful fail if attr not present.
  # Value if present.
  pass
