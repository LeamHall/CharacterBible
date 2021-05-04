#!/usr/bin/env python3

# name:     show_person.py
# version:  0.0.1
# date:     20210320
# author:   Leam Hall
# desc:     Demo of the Person and Character classes

import os
cwd = os.getcwd()
project_dir = os.path.dirname(cwd)
#libdir = project_dir + "/person"
import sys
#sys.path.append('/home/leam/lang/git/LeamHall/CharacterBible')
sys.path.append(project_dir)
print(sys.path)

from person.person import Person
from person.character import Character

date = 1429360

al = Person()
#{'first_name' : 'Alba', 'last_name': 'Domici', 'birth_year': 1416} )
# Really need a builder
#al.set_age(date)
al.modify_skill('Blade', 2)
for person in [al]:  
  print(person)


amanda = Person( 'Amanda Lefron', 1430000)

wilbur = Character( 'Wilbur Lefron', 1416075, 'Saorsa', 
     ['Firster Academy', 'Clan', 'Saorsa', 'Navy'])
#wilbur.set_age(date)
wilbur.gender = 'M'
wilbur_stat_data = {'str' : 9, 'dex': 7, 'end': 13, 'int': 9, 'edu': 10, 'soc': 11 }
wilbur.set_stats(wilbur_stat_data)
wilbur.modify_skill('Leader', 2)
for char in [wilbur]:
  print(char)
