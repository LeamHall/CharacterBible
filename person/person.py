#!/usr/bin/env python3

# name:     person.py
# version:  0.0.1
# date:     20210422
# author:   Leam Hall
# desc:     Base Person object.

from dataclasses import dataclass, field
# from typing import Any

@dataclass
class Person:
  """
  >>> al = Person()

  ''' Existing attributes '''
  >>> al.first_name = "Al"
  >>> al.first_name
  'Al'

  >>> al.add_attr('gender', 'F')
  >>> al.get_attr('gender')
  'F'

  >>> al.add_attr('last_name', "Lefron")
  >>> al.first_name + ' ' + al.last_name
  'Al Lefron'

  ''' Unspecified attributes '''
  >>> al.add_attr('zaniness', 'high')
  >>> al.get_attr('zaniness')
  'high'
  >>> al.get_attr('social grace') is None
  True

  ''' Skills '''
  >>> al.modify_skill('blade', 2)
  >>> al.get_skill('blade')
  2
  >>> al.get_skill('kissing') is None
  True

  """

  skills:     dict = field(default_factory=dict)
  physical:   str = ''
  mental:     str = ''
  first_name: str = ''
  last_name:  str = ''
  gender:     str = ''
  birth_year: int = 0
  birth_day:  int = 0
  notes:      str = ''


  def add_attr(self, attr, value):
    setattr(self, attr, value)

  def get_attr(self, attr):
    if hasattr(self, attr):
      return getattr(self,attr)
    else:
      return None

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

if __name__ == "__main__":
  import doctest
  doctest.testmod()
 
