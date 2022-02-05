#!/usr/bin/env python3

# name:     character.py
# version:  0.0.1
# date:     20210422
# author:   Leam Hall
# desc:     Object for 2d6 OGL Sci-Fi games.

from dataclasses import dataclass, field
from person import Person

@dataclass
class Character(Person):
  
  stats:      dict  = field(default_factory=dict)
  skills:     dict  = field(default_factory=dict)
  extras:     dict  = field(default_factory=dict)
  upp:        str   = None

  def gen_upp(self):
    ''' Specific to 2d6 Traveller type games'''
    upp_s = ''
    for stat in [ 'str', 'dex', 'end', 'int', 'edu', 'soc' ]:
      s = self.stats[stat]
      s = format(s, 'X')
      upp_s += str(s)
    self.upp = upp_s

  def get_stat(self, stat_name, form = 'int'):
    try:
      s = self.stats[stat_name]
    except KeyError:
      return None
    if form == 'hex':
      ''' Specific to 2d6 Traveller type games'''
      s = format(s, 'X')
    return s

  def set_stats(self, stat_data):
    self.stats = stat_data

  def set_extras(self, extra_data):
    if self.extras:
      self.extras |= extra_data
    else:
      self.extras = extra_data

  def get_skill(self, skill_name):
    if skill_name in self.skills:
      return self.skills[skill_name]
    else:
      return None

  def modify_skill(self, skill_name, value = 1): 
    if skill_name in self.skills:
      self.skills[skill_name] += value
    else:
      self.skills[skill_name] = value

  def supp_4(self):
    skill_list = []
    for skill in self.skills.keys():
      s = f"{skill}-{self.get_skill(skill)}"
      skill_list.append(s)
    skill_list.sort()
    skill_str = ", ".join(skill_list)
    output_string = ( f"{self.first_name} {self.last_name} [{self.gender.upper()}] {self.upp}",
      f"{skill_str}" )
    return output_string

