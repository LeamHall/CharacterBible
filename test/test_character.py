#!/usr/bin/env python3

# name:     test_character.py
# version:  0.0.1
# date:     20210422
# author:   Leam Hall
# desc:     Testing 2d6 OGL Character object

import unittest
from person import Person
from person import Character

class TestCharacter(unittest.TestCase):

  def setUp(self):
    self.stats     = {'str': 7, 'dex': 8, 'end':10, 'int':6, 'edu':7, 'soc': 12} 
    all_data  = { 'stats':self.stats }
    #self.data = {'first_name': 'Al', 'last_name': 'Lefron', 'gender': 'f', 'stats' : stats}
    self.al = Character(first_name = 'Al', last_name = 'Lefron', gender = 'f', 
      stats = self.stats)
    #self.al   = Character(self.data)

  def test_creation(self):
    # Note that this also tests "creation_empty_data".  :)
    #al = Character()
    self.assertIsInstance(self.al, Character)
    self.assertIsInstance(self.al, Person)

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
    valid_chars = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    self.al.set_stats(self.al.stats)
    self.al.gen_upp()
    #for char in self.al.upp:
    #  self.assertTrue(char in valid_chars)

  def test_get_stat(self):
    # Can pull a specific stat.
    # What if that stat doesn't exist?
    #  - unset
    #  - wrong game
    self.al.set_stats(self.stats)
    self.assertEqual(self.al.stats['soc'], 12)

  def test_get_stat_missing_int(self):
    self.assertEqual(self.al.get_stat('loop'), None)

  def test_get_stat_missing_hex(self):
    self.assertEqual(self.al.get_stat('loop', form='hex'), None)

  def test_modify_skill(self): 
    # Test if skill missing.
    # Test if skill can be lowered, and raised.
    # Is it reasonable to think something could delete the skills structure?
    pass

  def test_get_skill(self):
    # Get None if no skill.
    # Get number if has skill.
    pass

  def test_set_extras(self):
    extra_data = { 'rank':'CPT', 'service':'Dragon' }
    self.al.set_extras(extra_data)
    self.assertEqual(self.al.extras['rank'], 'CPT')
    self.assertEqual(self.al.extras['service'], 'Dragon')


if __name__ == "__main__":
  unittest.main()
