# name:     test_datamine.py
# version:  0.0.1
# date:     20211227
# author:   Leam Hall
# desc:     Test the datamine.

import pytest

from datamine import datamine

def test_datamine(dm):
  assert isinstance(dm, datamine.Datamine)

def test_basic_connect(dm):
  criteria  = {'table':'people'}
  result    = dm.select(criteria)  
  assert    len(result) > 100
  assert    len(result) < 200

def test_table_missing(dm):
  criteria  = {}
  with pytest.raises(KeyError):
    result = dm.select(criteria)

def test_select_splat(dm):
  criteria  = {'table':'people'}
  result    = dm.select(criteria)  
  assert    result[0] == (1, 'Romero', 'Cecil', None, 'm', 1413242, None, None, '')

def test_select_multicolumn(dm):
  criteria  = {'table':'people', 'columns': 'idx, first_name, last_name'}
  result    = dm.select(criteria)
  assert    result[0] == (1, 'Cecil', 'Romero' )

def test_select_multicolumn_with_limit(dm):
  criteria  = {'table':'people', 'columns': 'idx, first_name, last_name', 'limit' : 1}
  result    = dm.select(criteria)
  assert    result[0]    == (1, 'Cecil', 'Romero' )
  assert    len(result)  == 1

def test_select_multicolumn_with_limit_string(dm):
  criteria  = {'table':'people', 'columns': 'idx, first_name, last_name', 'limit' : '1'}
  result    = dm.select(criteria)
  assert    result[0]    == (1, 'Cecil', 'Romero' )
  assert    len(result)  == 1

def test_select_last_name_like(dm):
  criteria  = {'table':'people', 'columns': 'idx, first_name, last_name', 'limit' : '1', 'like_column' : 'last_name', 'like': 'Domici'}
  result    = dm.select(criteria)
  assert    result[0]    == (123, 'Alba', 'Domici' )
  assert    len(result)  == 1

def test_select_random_like_limit(dm):
  criteria  = {'table':'people', 'columns': 'last_name', 'like_column' : 'last_name', 'like': 'Domici', 'random' : True}
  result    = dm.select(criteria)
  assert    result[0]    == ('Domici', )
  assert    len(result)  == 1

@pytest.mark.skip("need to replace tests using plots") 
def test_select_one_random(dm):
  # Need to fix this since the plots table is going away. 
  criteria  = {'table':'plots'}
  result    = dm.select_one_random(criteria)
  assert    len(result) > 3
  assert    isinstance(result, str) 

def test_get_by_idx(dm):
  criteria  = {'table': 'people', 'idx':118 }
  result    = dm.get_by_idx(criteria)
  assert    result[0] == (118, 'Lefron', 'Wilbur', None, 'm', 1416075, None, None, 'Gimpy Rat')


def test_get_with_like(dm):
  criteria  = {'table':'people', 'like_column' : 'last_name', 'like': 'Domici'}
  result    = dm.select(criteria)
  assert    result[0]    == (123, 'Domici', 'Alba', None, 'f', 1416146, None, None, 'Trail Rat')
  assert    len(result)  == 1

