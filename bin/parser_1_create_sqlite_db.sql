-- parser_1_create_sqlite_db.sql
-- version: 0.0.1
-- date:    20201105
-- author:  Leam Hall 
-- desc:    Create a sample database for CharacterBible.


.headers    on
.mode       column
.nullvalue  [NULL]
.echo       on

DROP TABLE IF EXISTS cadets;

CREATE TABLE cadets (
  year        INTEGER NOT NULL,
  cadre       INTEGER NOT NULL,
  id          INTEGER NOT NULL,
  last_name   TEXT,
  first_name  TEXT,
  gender      TEXT,
  upp         TEXT,
  birth_year  INTEGER,
  birth_day   INTEGER,
  notes       TEXT,
  PRIMARY KEY (year, cadre, id)
);


