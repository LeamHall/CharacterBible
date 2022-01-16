# name:     datamine.py
# version:  0.0.1
# date:     20211227
# author:   Leam Hall
# desc:     Interface to data sources.

import os
import sqlite3

class Datamine:
  def __init__(self, file):
    self.con = sqlite3.connect(file)
  
  def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(self.cur.description):
      d[col[0]] = row[idx]
    return d

  def build_test_db(self, file):
    all_files = os.listdir('database')
    for file in all_files:
      if file.startswith("write_"):
        filename = os.path.join('database', file)
        with open(filename, 'r') as f:
          sqlcmd = f.read()
          self.con.executescript(sqlcmd)
    for file in all_files:
      if file.startswith("test_add_"):
        filename = os.path.join('database', file)
        with open(filename, 'r') as f:
          sqlcmd = f.read()
          self.con.executescript(sqlcmd) 
    return 
  
  def check_table_given(self, data): 
    if not data['table']:
      raise KeyError("Table name not provided")

  def select(self, data):
    self.check_table_given(data)
    self.cur    = self.con.cursor()
    table       = data['table']
    columns     = data.get('columns', '*')
    idx         = data.get('idx', None)
    like        = data.get('like', None) 
    like_column = data.get('like_column', None)
    random      = data.get('random', None)
    limit       = data.get('limit', None)

    select_statement = "SELECT {} FROM {}".format(columns, table)
    if idx:
      select_statement += " WHERE idx == {}".format(idx)
    if like_column and like:
      select_statement += " WHERE {} LIKE '{}'".format(like_column, like)
    if random:
      select_statement += " ORDER BY RANDOM()"
    if limit:
      select_statement += " LIMIT({})".format(int(limit))
    
    try:
      result = self.cur.execute(select_statement)
    except sqlite3.OperationalError:
      raise RuntimeError("table, column, or select issue")
    else:
      return result.fetchall()
    finally:
      self.cur.close()

  def select_one_random(self, data):
    self.check_table_given(data)
    data['random']  = True
    data['limit']   = 1
    result = self.select(data)
    return str(result[0][1])

  def remove_by_idx(self, data):
    self.cur = self.con.cursor()
    self.check_table_given(data)
    table   = data['table']
    idx     = data['idx']
    delete_statement = f"DELETE FROM {table} WHERE idx = {idx}"
    #try:
    result = self.cur.execute(delete_statement).rowcount
    self.con.commit()
    self.cur.close()
    #except sqlite3.OperationalError:
    #  raise RuntimeError("issue in remove_by_idx")
    #else:
    return result 

  def update_by_idx_column(self, data):
    self.cur = self.con.cursor()
    self.check_table_given(data)
    table   = data['table']
    idx     = data['idx']
    column  = data['column']
    value   = data['value']
    update_statement = f"UPDATE {table} SET {column}={value} WHERE idx = {idx}"
    result  = self.cur.execute(update_statement).rowcount
    self.con.commit()
    self.cur.close()
    return result 

  def get_by_idx(self, data):
    self.check_table_given(data)
    result = self.select(data)
    return result

  def get_with_like(self, data):
    self.check_table_given(data)
    result = self.select(data)
    return result

  def insert(self, data):
    """ self, dict with table and schema key/value pairs """
    self.check_table_given(data)
    self.cur = self.con.cursor()
    table       = data['table']
    columns     = []
    values      = []
    for column, value in data.items():
      if column == 'table':
        continue
      if any(ch.isalpha() for ch in value):
        value = f"'{value}'"
      columns.append(column)
      values.append(value)
    insert_statement = f"INSERT into {table} ({','.join(columns)}) VALUES ( {','.join(values)} )"
    #try:
    result = self.cur.execute(insert_statement)
    self.con.commit()
    self.cur.close()
    #except sqlite3.OperationalError:
    #  raise RuntimeError("INSERT issue")
    #except Exception as e:
    #  print(e)
    #else:
    #  return
    return result
    
  def dict_factory(self, cursor, row):
    d = {}
    for idx, col in enumerate(self.cur.description):
      d[col[0]] = row[idx]
    return d

  def keys(self, data):
    self.check_table_given(data)
    self.cur = self.con.cursor()
    try:
      table     = data['table']
      self.con.row_factory = self.dict_factory
      self.cur  = self.con.cursor()
      self.cur.execute(f"SELECT * from {table}")
      k         = self.cur.fetchone().keys()
    except sqlite3.OperationalError:
      raise RuntimeError("Keys issue")
    else:
      return list(k)
    finally:
      self.cur.close()

   
