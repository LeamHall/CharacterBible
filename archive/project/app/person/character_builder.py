#!/usr/bin/env python3

# name:     character_builder.py
# version:  0.0.1
# date:     20210612
# author:   Leam Hall
# desc:     Builder for Character Object

import random
from .character import Character
from .person import Person
from .person_builder import PersonBuilder

#  birth_year: int = 0
#  birth_day:  int = 0
#  notes:      str = ''


class CharacterBuilder:
    def build(self, data={}):
        self.set_person(data)
        self.set_character(data)
        self.set_stats(data)
        self.character.gen_upp()
        c = self.return_character()
        return c

    def set_person(self, data):
        self.person = data.get("person", self.gen_person())

    def set_character(self, data):
        # data['person'] = data.get('person', Person())
        data["person"] = data.get("person", self.person)
        self.character = Character(**data)

    def set_stats(self, data):
        stats = data.get("stats", {})
        stat_data = {}
        for stat in ["str", "dex", "end", "int", "edu", "soc"]:
            stat_data[stat] = stats.get(stat, self.roll_2d6())
        self.character.set_stats(stat_data)

    def roll_2d6(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def gen_person(self):
        person = Person()
        pb = PersonBuilder()
        p = pb.gen_data(person)
        return p

    def return_character(self):
        return self.character
