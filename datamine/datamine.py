# name:     datamine.py
# version:  0.0.1
# date:     20210423
# author:   Leam Hall
# desc:     Data abstraction object.

from dataclasses import dataclass

@dataclass
class DataMine:
  pass

  def get_person(self, character_id):
    ''' 
        A person could be a character, or a person. 
        Test with isinstance()
    '''
    pass

  def save_person(self, person_id):
    ''' 
        A person could be a character, or a person. 
        Test with isinstance()
    '''
    pass

if __name__ == '__main__':
  import doctest
  doctest.testmod()

