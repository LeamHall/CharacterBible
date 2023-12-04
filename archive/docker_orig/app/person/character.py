#!/usr/bin/env python3

# name:     character.py
# version:  0.0.1
# date:     20210422
# author:   Leam Hall
# desc:     Object for 2d6 OGL Sci-Fi games.

from dataclasses import dataclass, field
from person import Person


@dataclass
class Character(Person):
    """
    Note that these tests hit more than just Character specific attributes and
    methods. This is intentional.

    >>> al = Character()

    ''' Existing attributes '''
    >>> al.first_name = "Al"
    >>> al.first_name
    'Al'

    >>> al.set_attr('gender', 'F')
    >>> al.get_attr('gender')
    'F'

    >>> al.set_attr('last_name', "Lefron")
    >>> al.first_name + ' ' + al.last_name
    'Al Lefron'

    ''' Unspecified attributes '''
    >>> al.set_attr('zaniness', 'high')
    >>> al.get_attr('zaniness')
    'high'
    >>> al.get_attr('social grace') is None
    True

    ''' Stats '''
    >>> stat_data = {'str': 6, 'dex': 6, 'end': 10, 'int': 6, 'edu': 6, 'soc': 12 }
    >>> al.set_stats(stat_data)
    >>> al.gen_upp()
    >>> al.upp
    '66A66C'

    >>> al.get_stat('soc', 'hex')
    'C'
    >>> al.get_stat('soc')
    12

    ''' Skills '''
    >>> al.modify_skill('blade', 2)
    >>> al.get_skill('blade')
    2
    >>> al.get_skill('kissing') is None
    True

    ''' Supp 4 Output '''
    >>> al.supp_4()
    'Al Lefron [F] 66A66C'

    """

    skills: dict = field(default_factory=dict)
    stats: dict = field(default_factory=dict)
    upp: str = None

    def gen_upp(self):
        """Specific to 2d6 Traveller type games"""
        upp_s = ""
        for stat in ["str", "dex", "end", "int", "edu", "soc"]:
            s = self.stats[stat]
            s = format(s, "X")
            upp_s += str(s)
        self.upp = upp_s

    def get_stat(self, stat_name, form="int"):
        s = self.stats[stat_name]
        if form == "hex":
            """Specific to 2d6 Traveller type games"""
            s = format(s, "X")
        return s

    def set_stats(self, stat_data):
        self.stats = stat_data

    def get_skill(self, skill_name):
        if skill_name in self.skills:
            return self.skills[skill_name]
        else:
            return None

    def modify_skill(self, skill_name, value=1):
        if skill_name in self.skills:
            self.skills[skill_name] += value
        else:
            self.skills[skill_name] = value

    def supp_4(self):
        output_string = "{} {} [{}] {}".format(
            self.first_name, self.last_name, self.gender, self.upp
        )
        return output_string


if __name__ == "__main__":
    import doctest

    doctest.testmod()
