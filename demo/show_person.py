#!/usr/bin/env python3

# name:     show_person.py
# version:  0.0.2
# date:     20210612
# author:   Leam Hall
# desc:     Demo of the Person and Character classes

# This isn't a package yet, so the 'person' has to be added to sys.path.
import sys
sys.path.append('person')

from person import Person
from character import Character

date = 1429360

# Really need a builder
al = Person()
al.set_attr('first_name', 'Al')
al.set_attr('last_name', 'Lefron')
al.set_attr('gender', 'F')
al.set_attr('birth_year', 1416)
al.set_attr('birth_day', 146)
print("{} {} [{}]".format(al.first_name, al.last_name, al.gender))

amanda = Person()

wilbur = Character()
wilbur.set_attr('first_name', 'Wilbur')
wilbur.set_attr('last_name', 'Lefron')
wilbur.set_attr('gender', 'M')
w_stats = {'str' : 9, 'dex': 7, 'end': 13, 'int': 9, 'edu': 10, 'soc': 11 }
wilbur.set_stats(w_stats)
wilbur.gen_upp()
#print("{} {} [{}] {}".format(wilbur.first_name, wilbur.last_name, wilbur.gender, wilbur.upp))
print(wilbur.supp_4())
