-- write_people_table.sql
-- version: 0.0.2
-- date:    20201121
-- author:  Leam Hall
-- desc:    Create a sample 2d6 OGL people database.

-- changelog:
--   20201121 Changed plot and temperament to INTEGER, 
--     for their own tables.


DROP TABLE IF EXISTS people;

CREATE TABLE people (
  idx         INTEGER NOT NULL PRIMARY KEY,
  last_name   TEXT,
  first_name  TEXT,
  middle_name TEXT,
  gender      TEXT,
  birthdate   INTEGER,
  plot        INTEGER,
  temperament INTEGER,
  notes       TEXT
);


