-- name:    write_peopleskills_specializations_table.sql
-- version: 0.0.1
-- date:    20201128
-- author:  Leam Hall
-- desc:    Create a matrix of skill specilizations to people, skills.

.headers    on
.nullvalue  [NULL]

DROP TABLE IF EXISTS peopleskills_specializations;

CREATE TABLE peopleskills_specializations (
  id                INTEGER NOT NULL PRIMARY KEY,
  people_id         INTEGER,
  skill_id          INTEGER,
  specialization_id INTEGER,
  level             INTEGER
);
