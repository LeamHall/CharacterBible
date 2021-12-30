-- name:    write_temperaments_table.sql
-- version: 0.0.1
-- date:    20201121
-- author:  Leam Hall
-- desc:    Create a temperaments table.

.headers    on
.nullvalue  [NULL]
.echo       on

DROP TABLE IF EXISTS temperaments;

CREATE TABLE temperaments (
  idx          INTEGER NOT NULL PRIMARY KEY,
  temperament TEXT
);

