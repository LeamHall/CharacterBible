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

  first_name:     str   = ''
  last_name:      str   = ''
  gender:         str   = ''
  birth_info:     dict  = field(default_factory=dict)
  notes:          str   = ''
  idx:            int   = -1

  def set_attr(self, attr, value, key = None):
    # For the list and the dict, it assumes they already exist.
    try:
      attr_type = getattr(self, attr)
      if isinstance(attr_type, list):
        attr_type.append(value)
      elif isinstance(attr_type, dict) and key != None:
        if key:
          print("in dict, key is " + key)
        attr_type[key] = value
      else:
        attr_type = value
    except:
      setattr(self, attr, value)
 
  def get_attr(self, attr):
    if hasattr(self, attr):
      return getattr(self,attr)
    else:
      return None

if __name__ == "__main__":
  import doctest
  doctest.testmod()
 
