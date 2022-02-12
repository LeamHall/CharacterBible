-- name:    write_people_skill_level_table.sql
-- version: 0.0.1
-- date:    20220212
-- author:  Leam Hall
-- desc:    Create a matrix of skill levels to people.

DROP TABLE IF EXISTS people_skill_level;
CREATE TABLE people_skill_level (
  idx INTEGER PRIMARY KEY,
  people_idx  INTEGER NOT NULL REFERENCES people(idx),
  skill_idx   INTEGER NOT NULL REFERENCES skills(idx),
  skill_level INTEGER NOT NULL 
);

