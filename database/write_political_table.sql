-- name:    write_political_table.sql
-- version: 0.0.1
-- date:    20201207
-- author:  Leam Hall
-- desc:    Create a sample political affiliation table.

.headers    on
.nullvalue  [NULL]
.echo       on

DROP TABLE IF EXISTS political;

CREATE TABLE political (
  id        INTEGER NOT NULL PRIMARY KEY,
  political INTEGER
);

