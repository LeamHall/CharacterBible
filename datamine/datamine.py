# name:     datamine.py
# version:  0.0.1
# date:     20211227
# author:   Leam Hall
# desc:     Interface to data sources.


import sqlite3

class Datamine:
  def __init__(self, file):
    self.con = sqlite3.connect(file)
    self.cur = self.con.cursor()
  
  def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(self.cur.description):
      d[col[0]] = row[idx]
    return d
  
  def check_table_given(self, data): 
    if not data['table']:
      raise KeyError("Table name not provided")

  def select(self, data):
    self.check_table_given(data)
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

  def select_one_random(self, data):
    self.check_table_given(data)
    data['random']  = True
    data['limit']   = 1
    result = self.select(data)
    return str(result[0][1])


  def get_by_idx(self, data):
    self.check_table_given(data)
    result = self.select(data)
    return result

  def get_with_like(self, data):
    self.check_table_given(data)
    result = self.select(data)
    return result

