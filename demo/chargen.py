#!/usr/bin/env python3

# name:     chargen.py
# version:  0.0.1
# date:     20210612
# author:   Leam Hall
# desc:     Create Person and Character Objects

### Notes
# Must be copied into the directory holding the library directory.

import sys
sys.path.append('person')

from person import Person
from character import Character
from character_builder import CharacterBuilder

stats     = {'soc': 13}
data      = {'first_name': 'Amanda', 'last_name': 'Lefron', 'gender': 'F', 'stats' : stats}
builder   = CharacterBuilder(data)
character = builder.return_character()
print(character.supp_4())

##
#  birth_year: int = 0
#  birth_day:  int = 0
#  notes:      str = ''
#

