-- name:    write_planets_table.sql
-- version: 0.0.1
-- date:    20201207
-- author:  Leam Hall
-- desc:    Create a sample planets table.


DROP TABLE IF EXISTS planets;

CREATE TABLE planets (
  idx        INTEGER NOT NULL PRIMARY KEY,
  planet    TEXT,
  political INTEGER
);

