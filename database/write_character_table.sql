-- write_character_table.sql
-- version:   0.0.1
-- date:      20201111
-- author:    Leam Hall
-- desc:      Add 2d6 OGL character data table to a database.


DROP TABLE IF EXISTS chars_2d6ogl;

CREATE TABLE chars_2d6ogl (
  idx        INTEGER NOT NULL PRIMARY KEY,
  str       INTEGER,
  dex       INTEGER,
  end       INTEGER,
  int       INTEGER,
  edu       INTEGER,
  soc       INTEGER,
  psr       INTEGER,
  people_id INTEGER NOT NULL REFERENCES people( idx )
);


