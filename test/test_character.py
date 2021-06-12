#!/usr/bin/env python3

# name:     test_character.py
# version:  0.0.1
# date:     20210422
# author:   Leam Hall
# desc:     Testing 2d6 OGL Character object

# This isn't a package yet, so the 'person' has to be added to sys.path.
import sys
sys.path.append('person')

import unittest
#from person.character import Character
#from person.person import Person
#from person.person import Person as Person
#from person.character import Character as Character
#from person import Person
from person import Character

#from person import Person

class TestCharacter(unittest.TestCase):

  def test_creation(self):
    # Note that this also tests "creation_empty_data".  :)
    al = Character()
    self.assertIsInstance(al, Character)
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

  def test_gen_upp(self):
    # Given a valid set of stats, can generate a UPP string.
    # Does this need a different process, since it doesn't cover
    # 3d6 and d% games?
    # What if numbers for UPP are:
    #  - missing
    #  - invalid ( < 0 or > 15)
    pass

  def test_get_stat(self):
    # Can pull a specific stat.
    # What if that stat doesn't exist?
    #  - unset
    #  - wrong game
    pass
     
  def test_set_stats(self):
    # Can set stats post instance creation.
    # What if only some stats are given?
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
