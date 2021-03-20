#!/usr/bin/env python3

# name:     show_person.py
# version:  0.0.1
# date:     20210320
# author:   Leam Hall
# desc:     Demo of the Person and Character_2d6 classes

# This isn't a package yet, so the 'lib' has to be added to sys.path.
import sys
sys.path.append('lib')

from person import Person
from character_2d6 import Character_2d6

date = 1429360

al = Person( 'Alba Ester Domici', 1416146, 'Birach', 
      ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'])
# Really need a builder
al.set_age(date)
for person in [al]:  
  print(person)


amanda = Person( 'Amanda Lefron', 1430000)

wilbur = Character_2d6( 'Wilbur Lefron', 1416075, 'Saorsa', 
     ['Firster Academy', 'Clan', 'Saorsa', 'Navy'])
wilbur.set_age(date)
wilbur.gender = 'M'
wilbur.stats = {'str' : 9, 'dex': 7, 'end': 13, 'int': 9, 'edu': 10, 'soc': 11 }
wilbur.set_upp()

for char in [wilbur]:
  print(char)
