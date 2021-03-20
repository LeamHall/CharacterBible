# name:     character_2d6.py
# version:  0.0.1
# date:     20210320
# author:   Leam Hall
# desc:     Uses Person, adds 2d6 game stuff.


from person import Person

class Character_2d6(Person):
  
  def __init__(self, name = '', birth_date = 0, birth_world = '', 
    cultures = [], gender = 'F', age = 'unborn', stats = {}, 
    skills = {}, career = ''):
    """
    (Character_2d6, str, int, str, list, str, int, dict, dict, str) -> NoneType
  
    Creates a new Character_2d6, expanding on what the Person class does.

    >>> al = Character_2d6 ( \
                'Alba Ester Domici', 1416146, 'Birach', \
                ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'], \
                'F', '', {}, {}, 'Noble') 
    >>> al.name
    'Alba Ester Domici'
    >>> al.career
    'Noble'
    
    """

    super().__init__( name, birth_date, birth_world, cultures, gender)
    self.career = career


  def set_upp(self):
    """ 
    (Character_2d6) -> NoneType

    Requires the UPP stats to already be set.
    Sets the UPP based on the character's stats.

    >>> al = Character_2d6 ( \
                'Alba Ester Domici', 1416146, 'Birach', \
                ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'], \
                'F', '', {}, {}, 'Noble') 
    >>> al.stats = {'str' : 8, 'dex': 7, 'end': 11, 'int': 6, 'edu': 8, 'soc': 12 }
    >>> al.set_upp()
    >>> al.upp
    '87B68C'
    """

    # Need an error process that fails gracefully if the stat isn't defined.
    upp_string = ''
    for stat in [ 'str', 'dex', 'end', 'int', 'edu', 'soc']:
      upp_string += "{:X}".format(self.stats[stat])

    self.upp = upp_string


  def __str__(self):
    """
    (Character_2d6) -> str

    Return a standard Traveller output of the Person
  
    >>> al = Character_2d6( \
              'Alba Ester Domici', 1416146, 'Birach', \
              ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'] \
              )
    >>> al.set_age(1429360)
    >>> al.stats = {'str' : 8, 'dex': 7, 'end': 11, 'int': 6, 'edu': 8, 'soc': 12 }
    >>> al.set_upp()
    >>> print(al)
    Alba Ester Domici [87B68C] F Age: 13
    """

    return "{0} [{1}] {2} Age: {3}".format(self.name, self.upp, self.gender, self.age)


if __name__ == '__main__':
  import doctest
  doctest.testmod()
    
