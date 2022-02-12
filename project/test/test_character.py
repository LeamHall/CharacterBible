#!/usr/bin/env python3

# name:     test_character.py
# version:  0.0.2
# date:     20220212
# author:   Leam Hall
# desc:     Testing 2d6 OGL Character object
#
# CHANGELOG
#   20220212  Refactor to pytest

import pytest
from app.person import Person
from app.person import Character

def test_creation(character):
  assert isinstance(character, Character)

def test_creation_full_data():
  # Can add an existing person's data
  pass

def test_add_attr():
  # Can add an attr.
  # Replaces existing attr with new value.
  pass

def test_get_attr():
  # Graceful fail if attr not present.
  # Value if present.
  pass

def test_gen_upp(character):
# Given a valid set of stats, can generate a UPP string.
  # stat generation is currently in character_builder.
  valid_chars = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  character.gen_upp()
  for char in character.upp:
    assert (char in valid_chars)
  assert (character.upp == '78A67C')

def test_get_stat(character):
  assert (character.stats['soc'] == 12)

def test_get_stat_hex(character):
  assert(character.get_stat('soc', form='hex') == 'C')

def test_get_stat_missing_int(character):
  assert(character.get_stat('loop') == None)

def test_get_stat_missing_hex(character):
  assert(character.get_stat('loop', form='hex') == None)

def test_modify_skill_present(character): 
  character.modify_skill('Kissing', 2)
  assert(character.get_skill("Kissing") == 4)

def test_modify_skill_missing(character):
  character.modify_skill('Blade', 1)
  assert(character.get_skill("Blade") == 1)

def test_modify_skill_lower(character):
  character.modify_skill('Kissing', -1)
  assert(character.get_skill("Kissing") == 1)

def test_get_skill_present(character):
  assert(character.get_skill("Kissing") == 2)

def test_get_skill_missing(character):
  assert(character.get_skill("Pilot") == None)

def test_set_extras(character):
  extra_data = { 'rank':'CPT', 'service':'Dragon' }
  character.set_extras(extra_data)
  assert(character.extras['rank'] == 'CPT')
  assert(character.extras['service'] == 'Dragon')

def test_set_extras_even_more(character):
  extra_data = { 'rank':'CPT', 'service':'Dragon' }
  more_extra_data = { 'assignment':'BMM', 'rank':'PVT' }
  character.set_extras(extra_data)
  character.set_extras(more_extra_data)
  assert(character.extras['rank'] == 'PVT')
  assert(character.extras['service'] == 'Dragon')
  assert(character.extras['assignment'] == 'BMM')

def test_set_stats(character):
  stats = {'str': 8, 'dex':9, 'end':10, 'int':6, 'edu':7, 'soc':12 }
  character.set_stats(stats)
  assert(character.get_stat('str') == 8)

def test_supp_4(character):
  character.gen_upp()
  expected = ("Alba Domici [F] 78A67C", "GunCbt(CbtR)-2, Kissing-2, Math-0")
  assert(character.supp_4() == expected)
