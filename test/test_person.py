#!/usr/bin/env python3

import sys
sys.path.append('lib')

import unittest
from person import Person

class TestPerson(unittest.TestCase):

  def test_name(self):
    al = Person( 'Alba Ester Domici', 1416146, 'Birach', 
      ['Firster', 'Saorsa', 'Domici', 'Firster Academy', 'Clan', 'Dragon'])
    expected = 'Alba Ester Domici'
    actual    = al.name
    self.assertEqual(expected, actual, "Testing the name attribute.")


   
if __name__ == '__main__':
  unittest.main(exit = False) 

