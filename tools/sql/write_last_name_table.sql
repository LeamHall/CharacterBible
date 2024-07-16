-- write_last_name_table.sql
-- version: 0.0.1
-- date:    20240716
-- author:  Leam Hall
-- desc:    Add last name data for chargen.db

-- changelog:


DROP TABLE IF EXISTS last_name;

CREATE TABLE last_name (
  name   varchar[20] UNIQUE
);


