-- name:    write_plots_table.sql
-- version: 0.0.1
-- date:    20201121
-- author:  Leam Hall
-- desc:    Create a sample plots table.


DROP TABLE IF EXISTS plots;

CREATE TABLE plots (
  idx    INTEGER NOT NULL PRIMARY KEY,
  plot  TEXT
);

