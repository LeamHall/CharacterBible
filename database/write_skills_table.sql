-- name:    write_skills_table.sql
-- version: 0.0.1
-- date:    20201119
-- author:  Leam Hall
-- desc:    Create a sample Cepheus Engine skills table.


DROP TABLE IF EXISTS skills;

CREATE TABLE skills (
  idx    INTEGER NOT NULL PRIMARY KEY,
  skill TEXT
);

