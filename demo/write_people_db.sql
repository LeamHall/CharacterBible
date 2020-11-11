-- write_people_db.sql
-- version: 0.0.1
-- date:    20201107
-- author:  Leam Hall
-- desc:    Create a sample 2d6 OGL people database.

.headers    on
.nullvalue  [NULL]
.echo       on

DROP TABLE IF EXISTS people;

CREATE TABLE people (
  id          INTEGER NOT NULL PRIMARY KEY,
  last_name   TEXT,
  first_name  TEXT,
  middle_name TEXT,
  suffix_name TEXT,
  other_name  TEXT,
  gender      TEXT,
  birthdate   INTEGER,
  plot        TEXT,
  temperament TEXT,
  notes       TEXT
);


