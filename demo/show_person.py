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

date = 1429360

al = Person( 'Alba Ester Domici', 1416146, 'Birach', 
      ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'])

# Really need a builder
al.set_age(date)

# This needs to go into the game specific module.
al.stats = {'str' : 8, 'dex': 7, 'end': 11, 'int': 6, 'edu': 8, 'soc': 12 }
al.set_upp()

wilbur = Person( 'Wilbur Lefron', 1416075, 'Saorsa', 
     ['Firster Academy', 'Clan', 'Saorsa', 'Navy'])
wilbur.set_age(date)
wilbur.gender = 'M'

amanda = Person( 'Amanda Lefron', 1430000)

#for person in [al, wilbur, amanda]:
for person in [al]:  
  print(person)
