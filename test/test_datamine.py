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
  assert    len(result) == 1

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
  criteria  = {'table':'people', 'columns': 'idx, first_name, last_name', 'limit' : '1', 'like_column' : 'last_name', 'like': 'Romero'}
  result    = dm.select(criteria)
  assert    result[0]    == (1, 'Cecil', 'Romero' )
  assert    len(result)  == 1

def test_select_random_like_limit(dm):
  criteria  = {'table':'people', 'columns': 'last_name', 'like_column' : 'first_name', 'like': 'Cecil', 'random' : True}
  result    = dm.select(criteria)
  assert    result[0]    == ('Romero', )
  assert    len(result)  == 1

def test_get_by_idx(dm):
  criteria  = {'table': 'people', 'idx':1 }
  result    = dm.get_by_idx(criteria)
  assert    result[0] == (1, 'Romero', 'Cecil', None, 'm', 1413242, None, None, '')

def test_get_with_like(dm):
  criteria  = {'table':'people', 'like_column' : 'first_name', 'like': 'Cecil'}
  result    = dm.select(criteria)
  assert    result[0]   == (1, 'Romero', 'Cecil', None, 'm', 1413242, None, None, '')
  assert    len(result) == 1

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

def test_remove_by_idx(dm):
  insert_criteria = {'table':'people', 'last_name':'Domici', 'first_name':'Marco'}
  insert_result   = dm.insert(insert_criteria)
  select_criteria = { 'table':'people', 'like_column' : 'last_name', 'like': 'Domici'}
  result_t        = dm.select(select_criteria)
  idx             = result_t[-1][0]
  delete_criteria = { 'table': 'people', 'idx': idx }
  result          = dm.remove_by_idx(delete_criteria)
  assert result   == 1

def test_update_by_idx_column(dm):
  update_criteria = {'table':'people', 'idx':1, 'column':'plot', 'value':22}
  result          = dm.update_by_idx_column(update_criteria)
  assert result   == 1

