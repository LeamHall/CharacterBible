#!/usr/bin/env python3

# name:     test_character_builder.py
# version:  0.0.1
# date:     20210612
# author:   Leam Hall
# desc:     Testing Character Builder

import unittest

#import sys
#sys.path.append('person')
from person import Person
from person import Character
from person import CharacterBuilder

#stats     = {'soc': 13}
#data      = {'first_name': 'Amanda', 'last_name': 'Lefron', 'gender': 'F', 'stats' : stats}
#builder   = CharacterBuilder(data)
#character = builder.return_character()
#print(character.supp_4())
class TestCharacterBuilder(unittest.TestCase):

  def testCreation(self):
    builder = CharacterBuilder()
    character = builder.return_character()
    self.assertIsInstance(builder, CharacterBuilder)
    self.assertIsInstance(character, Character)
    self.assertIsInstance(character, Person)

  def testCreateName(self):
    data = {'first_name' : 'Amanda', 'last_name': 'Lefron'}
    builder = CharacterBuilder(data)
    character = builder.return_character()
    self.assertEqual(character.first_name, 'Amanda')
    self.assertEqual(character.last_name, 'Lefron')

  def testCreateStats(self):
    stats     = {'soc': 12}
    data      = {'first_name': 'Amanda', 'last_name': 'Lefron', 'gender': 'F', 'stats' : stats}
    builder = CharacterBuilder(data)
    character = builder.return_character()
    self.assertEqual(character.stats['soc'], 12)
    for s in character.stats.keys():
      self.assertGreaterEqual(character.stats[s], 2)
      self.assertLessEqual(character.stats[s], 12)



