#!/usr/bin/env python

import sys
sys.path.append("../project")
#print(sys.path)

from app.person import Person
from app.person.person_builder import PersonBuilder
from app.person import Character
from app.person import CharacterBuilder

pb = PersonBuilder()
p1 = pb.gen_data(Person())

print(p1)

cb  = CharacterBuilder()
c1  = cb.build()
print(c1.supp_4())
