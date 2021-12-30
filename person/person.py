#!/usr/bin/env python3

# name:     person.py
# version:  0.0.1
# date:     20210422
# author:   Leam Hall
# desc:     Base Person object.

from dataclasses import dataclass, field

@dataclass
class Person:
  """ Base Person object """

  idx:            int = -1
  last_name:      str = ''
  first_name:     str = ''
  middle_name:    str = ''
  gender:         str = ''
  birthdate:      int = ''
  plot:           str = ''
  temperament:    str = ''
  notes:          str = ''

  def set_attr(self, attr, value, key = None):
    setattr(self, attr, value)
 
  def get_attr(self, attr):
    if hasattr(self, attr):
      return getattr(self,attr)
    else:
      return None
