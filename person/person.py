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
  """ Base Person object """

  physical:       list  = field(default_factory=list)
  mental:         dict  = field(default_factory=dict)
  first_name:     str   = ''
  last_name:      str   = ''
  gender:         str   = ''
  birth_info:     dict  = field(default_factory=dict)
  notes:          str   = ''
  relationships:  dict  = field(default_factory=dict)
  culturesr:      list  = field(default_factory=list)

  def set_attr(self, attr, value, key = None):
    # For the list and the dict, it assumes they already exist.
    attr_type = getattr(self, attr)
    if isinstance(attr_type, list):
      self.attr.append(value)
    elif isinstance(attr_type, dict) and key != None:
      self.attr[key] = value
    else:
      setattr(self, attr, value)
  
  def get_attr(self, attr):
    if hasattr(self, attr):
      #return getattr(self,attr)
      return self.attr
    else:
      return None

if __name__ == "__main__":
  import doctest
  doctest.testmod()
 
