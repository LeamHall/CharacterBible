#!/usr/bin/env python3

# name:     character_builder.py
# version:  0.0.1
# date:     20210612
# author:   Leam Hall
# desc:     Builder for Character Object

import random
from person import Character
from person import Person
#from character import Character

#import person

#  physical:   str = ''
#  mental:     str = ''
#  birth_year: int = 0
#  birth_day:  int = 0
#  notes:      str = ''

class CharacterBuilder:
 
  def __init__(self, data = {}):
    self.character = Character()
    self.set_stats(data)
    self.set_data(data)
    self.character.gen_upp()
    self.return_character()
    

  def set_stats(self, data):
    stats = data.get('stats', {})
    stat_data = {}
    for stat in ['str', 'dex', 'end', 'int', 'edu', 'soc']:
      stat_data[stat] = stats.get(stat, self.roll_2d6())
    self.character.set_stats(stat_data)
      

  def roll_2d6(self):
    return random.randint(1,6) + random.randint(1,6)
 
  def set_data(self, data):
    self.character.gender     = data.get('gender', self.gen_gender())
    self.character.first_name = data.get('first_name', self.gen_first_name(self.character.gender))
    self.character.last_name  = data.get('last_name', self.gen_last_name())

  def gen_gender(self):
    return 'M'

  def gen_first_name(self, gender):
    return 'Fred'

  def gen_last_name(self):
    return 'Smith'

  def return_character(self):
    return self.character
  
  
