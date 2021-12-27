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
   
  def check_table_given(self, data): 
    if not data['table']:
      raise KeyError("Table name not provided")

  def select(self, data):
    self.check_table_given(data)
    table   = data['table']
    columns     = data.get('columns', '*')
    like        = data.get('like', None) 
    like_column = data.get('like_column', None)
    random      = data.get('random', None)
    limit       = data.get('limit', None)

    select_statement = "SELECT {} FROM {}".format(columns, table)
    if like_column and like:
      select_statement += " WHERE {} LIKE '{}'".format(like_column, like)
    if random:
      select_statement += " ORDER BY RANDOM()"
    if limit:
      select_statement += " LIMIT({})".format(int(limit))
    data = self.cur.execute(select_statement)

    return data.fetchall()

  def select_one_random(self, data):
    self.check_table_given(data)
    table   = data['table']
    data['random']  = True
    data['limit']   = 1
    result = self.select(data)
    return str(result[0][1])



