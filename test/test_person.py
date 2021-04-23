#!/usr/bin/env python3

# name:     test_person.py
# version:  0.0.1
# date:     20210422
# author:   Leam Hall
# desc:     Testing Base Person object.

import unittest
from person.person import Person as Person

class TestPerson(unittest.TestCase):

  def test_creation(self):
    # Note that this also tests "creation_empty_data".  :)
    al = Person()
    self.assertIsInstance(al, Person)

  def test_creation_full_data(self):
    # Can add an existing person's data
    pass

  def test_add_attr(self):
    # Can add an attr.
    # Replaces existing attr with new value.
    pass

  def test_get_attr(self):
    # Graceful fail if attr not present.
    # Value if present.
    pass

  def test_modify_skill(self): 
    # Test if skill missing.
    # Test if skill can be lowered, and raised.
    # Is it reasonable to think something could delete the skills structure?
    pass

  def test_get_skill(self):
    # Get None if no skill.
    # Get number if has skill.
    pass


if __name__ == "__main__":
  unittest.main()
