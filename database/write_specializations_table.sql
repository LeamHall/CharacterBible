-- name:    write_specializations_table.sql
-- version: 0.0.1
-- date:    20201128
-- author:  Leam Hall
-- desc:    Create a list of specializations.

.headers    on
.nullvalue  [NULL]

DROP TABLE IF EXISTS specializations;

CREATE TABLE specializations (
  idx              INTEGER NOT NULL PRIMARY KEY,
  specialization  INTEGER
);
