-- name:    write_cultures_table.sql
-- version: 0.0.1
-- date:    20201207
-- author:  Leam Hall
-- desc:    Create a sample cultural background table.

.headers    on
.nullvalue  [NULL]
.echo       on

DROP TABLE IF EXISTS cultures;

CREATE TABLE cultures (
  idx        INTEGER NOT NULL PRIMARY KEY,
  culture INTEGER
);

