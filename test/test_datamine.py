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
  criteria  = {'table':'people', 'columns': 'last_name', 'like_column' : 'first_name', 'like': 'Alba', 'random' : True}
  result    = dm.select(criteria)
  assert    result[0]    == ('Domici', )
  assert    len(result)  == 1

def test_get_by_idx(dm):
  criteria  = {'table': 'people', 'idx':118 }
  result    = dm.get_by_idx(criteria)
  assert    result[0] == (118, 'Lefron', 'Wilbur', None, 'm', 1416075, None, None, 'Gimpy Rat')

def test_get_with_like(dm):
  criteria  = {'table':'people', 'like_column' : 'first_name', 'like': 'Alba'}
  result    = dm.select(criteria)
  assert    result[0]    == (123, 'Domici', 'Alba', None, 'f', 1416146, None, None, 'Trail Rat')
  assert    len(result)  == 1

def test_insert(dm):
  criteria  = { 'table':'people', 'last_name':'Domici', 'first_name':'Marco' }
  criteria2 = { 'table':'people', 'like_column' : 'last_name', 'like': 'Domici'}
  result    = dm.insert(criteria)
  result_t  = dm.select(criteria2)
  assert    result_t[-1][2] == 'Marco'

def test_keys_people(dm):
  criteria  = { 'table':'people' }
  result    = dm.keys(criteria)
  assert result == ['idx', 'last_name', 'first_name', 'middle_name', 'gender', 'birthdate', 'plot', 'temperament', 'notes']


def test_keys_plots(dm):
  criteria  = { 'table':'plots' }
  result    = dm.keys(criteria)
  assert result == ['idx', 'plot']

