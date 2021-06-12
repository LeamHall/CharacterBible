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

  >>> al.set_attr('gender', 'F')
  >>> al.get_attr('gender')
  'F'

  >>> al.set_attr('last_name', "Lefron")
  >>> al.first_name + ' ' + al.last_name
  'Al Lefron'

  ''' Unspecified attributes '''
  >>> al.set_attr('zaniness', 'high')
  >>> al.get_attr('zaniness')
  'high'
  >>> al.get_attr('social grace') is None
  True


  """

  physical:   str = ''
  mental:     str = ''
  first_name: str = ''
  last_name:  str = ''
  gender:     str = ''
  birth_year: int = 0
  birth_day:  int = 0
  notes:      str = ''


  def set_attr(self, attr, value):
    setattr(self, attr, value)

  def get_attr(self, attr):
    if hasattr(self, attr):
      return getattr(self,attr)
    else:
      return None

if __name__ == "__main__":
  import doctest
  doctest.testmod()
 
