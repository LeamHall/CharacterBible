-- write_female_first_name_table.sql
-- version: 0.0.1
-- date:    20240716
-- author:  Leam Hall
-- desc:    Add female first name data for chargen.db

-- changelog:


DROP TABLE IF EXISTS female_first_name;

CREATE TABLE female_first_name (
  name   varchar[20] UNIQUE
);


