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
    self.stats  = { 'str': 7, 'dex': 8, 'end':10, 'int':6, 'edu':7, 'soc': 12 } 
    self.skills = { "GunCbt('CbtR')": 2, "Math": 0, "Kissing": 2 }
    self.data   = { 'first_name': 'Al', 'last_name': 'Lefron', 'gender': 'f', 
      'stats': self.stats, 'skills':self.skills }
    self.al     = Character(**self.data)

  def test_creation(self):
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
    # stat generation is currently in character_builder.
    valid_chars = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    self.al.gen_upp()
    for char in self.al.upp:
      self.assertTrue(char in valid_chars)
    self.assertEqual(self.al.upp, '78A67C')

  def test_get_stat(self):
    self.assertEqual(self.al.stats['soc'], 12)

  def test_get_stat_hex(self):
    self.assertEqual(self.al.get_stat('soc', form='hex'), 'C')

  def test_get_stat_missing_int(self):
    self.assertEqual(self.al.get_stat('loop'), None)

  def test_get_stat_missing_hex(self):
    self.assertEqual(self.al.get_stat('loop', form='hex'), None)

  def test_modify_skill_present(self): 
    self.al.modify_skill('Kissing', 2)
    self.assertEqual(self.al.get_skill("Kissing"), 4)

  def test_modify_skill_missing(self):
    self.al.modify_skill('Blade', 1)
    self.assertEqual(self.al.get_skill("Blade"), 1)

  def test_modify_skill_lower(self):
    self.al.modify_skill('Kissing', -1)
    self.assertEqual(self.al.get_skill("Kissing"), 1)

  def test_get_skill_present(self):
    self.assertEqual(self.al.get_skill("Kissing"), 2)

  def test_get_skill_missing(self):
    self.assertEqual(self.al.get_skill("Pilot"), None)
  
  def test_set_extras(self):
    extra_data = { 'rank':'CPT', 'service':'Dragon' }
    self.al.set_extras(extra_data)
    self.assertEqual(self.al.extras['rank'], 'CPT')
    self.assertEqual(self.al.extras['service'], 'Dragon')

  def test_set_extras_even_more(self):
    extra_data = { 'rank':'CPT', 'service':'Dragon' }
    more_extra_data = { 'assignment':'BMM', 'rank':'PVT' }
    self.al.set_extras(extra_data)
    self.al.set_extras(more_extra_data)
    self.assertEqual(self.al.extras['rank'], 'PVT')
    self.assertEqual(self.al.extras['service'], 'Dragon')
    self.assertEqual(self.al.extras['assignment'], 'BMM')

  def test_set_stats(self):
    stats = {'str': 8, 'dex':9, 'end':10, 'int':6, 'edu':7, 'soc':12 }
    self.al.set_stats(stats)
    self.assertEqual(self.al.get_stat('str'), 8)

  def test_supp_4(self):
    self.al.gen_upp()
    expected = ("Al Lefron [F] 78A67C", "GunCbt('CbtR')-2, Kissing-2, Math-0")
    self.assertEqual(self.al.supp_4(), expected)

if __name__ == "__main__":
  unittest.main()
