#!/usr/bin/env python3

# name:     test_character_builder.py
# version:  0.0.1
# date:     20210612
# author:   Leam Hall
# desc:     Testing Character Builder

import unittest

from app.person import Person
from app.person import Character
from app.person import CharacterBuilder

class TestCharacterBuilder(unittest.TestCase):
  def setUp(self):
    stats     = {'soc': 12}
    data      = {'first_name': 'Amanda', 'last_name': 'Lefron', 'gender': 'F', 'stats' : stats}
    self.builder = CharacterBuilder(data)
    self.character = self.builder.return_character()
  
  def testCreation(self):
    self.assertIsInstance(self.builder, CharacterBuilder)
    self.assertIsInstance(self.character, Character)
    self.assertIsInstance(self.character, Person)

  def testCreateName(self):
    self.assertEqual(self.character.first_name, 'Amanda')
    self.assertEqual(self.character.last_name, 'Lefron')

  def testCreateStats(self):
    self.assertEqual(self.character.stats['soc'], 12)
    for s in self.character.stats.keys():
      self.assertGreaterEqual(self.character.stats[s], 2)
      self.assertLessEqual(self.character.stats[s], 12)

  def test_set_extras(self):
    extra_data = { 'rank':'CPT', 'service':'Dragon' }
    self.character.set_extras(extra_data)
    self.assertEqual(self.character.extras['rank'], 'CPT')
    self.assertEqual(self.character.extras['service'], 'Dragon')

 
