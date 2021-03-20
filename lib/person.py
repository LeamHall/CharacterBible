# person.py

class Person:

  def __init__(self, name = '', birth_date = 0, birth_world = '', cultures = [], stats = {}, gender = 'F', age = 'unborn' ):
    """
    (Person, str, int, str, list of str) ->NoneType
    
    Create a new person, with a name, when and where they were born,
    and what cultures they are a member of.

    >>> al = Person ( \
              'Alba Ester Domici', 1416146, 'Birach', \
              ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'] \
              )
    >>> al.name
    'Alba Ester Domici'
    >>> al.cultures
    ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon']
    >>> al.birth_date
    1416146
    >>> al.birth_world
    'Birach'

    """

    self.name         = name
    self.birth_date   = int(birth_date)
    self.birth_world  = birth_world
    self.cultures     = cultures[:]
    self.gender       = gender
    self.stats        = stats
    self.age          = age

    
  def get_age(self, year):
    """
    (Person, Int) -> Int

    Returns the person's age, in (360 day) years, based on the given date.

    >>> al = Person ( \
              'Alba Ester Domici', 1416146, 'Birach', \
              ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'] \
              )
    >>> al.get_age(1429360)
    13

    """

    years = ( int(year) - self.birth_date ) // 1000
    if years < 0:
      years = 'unborn'
    return years


  def set_age(self, year):
    """
    (Person, Int) => NonType

    Sets the age attribute, in (360 day) years, based on the given date.

    >>> al = Person ( \
              'Alba Ester Domici', 1416146, 'Birach', \
              ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'] \
              )
    >>> al.set_age(1429360)
    >>> al.age
    13
    """

    years = ( year - self.birth_date) // 1000
    self.age = years


  def set_upp(self):
    """
    (Person) -> NoneType

    Requires the UPP stats to already be set.
    Sets the UPP based on the character's stats.

    >>> al = Person ( \
              'Alba Ester Domici', 1416146, 'Birach', \
              ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'] \
              )
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


  def num_cultures(self):
    """
    (Person) -> Int

    Return the number of cultures a person is a member of.

    >>> al = Person ( \
              'Alba Ester Domici', 1416146, 'Birach', \
              ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'] \
              )
    >>> al.num_cultures()
    6
    """

    return len(self.cultures)


  def __str__(self):
    """
    (Person) -> str

    Return a standard Traveller output of the Person
  
    >>> al = Person ( \
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


if __name__ == "__main__":
  import doctest
  doctest.testmod()

