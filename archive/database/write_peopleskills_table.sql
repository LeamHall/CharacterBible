-- name:    write_peopleskills_table.sql
-- version: 0.0.1
-- date:    20201128
-- author:  Leam Hall
-- desc:    Create a matrix of skills to people.

.headers    on
.nullvalue  [NULL]

DROP TABLE IF EXISTS peopleskills;

CREATE TABLE peopleskills (
  id        INTEGER NOT NULL PRIMARY KEY,
  people_id INTEGER,
  skill_id  INTEGER,
  level     INTEGER
);
