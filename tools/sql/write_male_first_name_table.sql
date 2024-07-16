-- write_male_first_name_table.sql
-- version: 0.0.1
-- date:    20240716
-- author:  Leam Hall
-- desc:    Add male first name data for chargen.db

-- changelog:


DROP TABLE IF EXISTS male_first_name;

CREATE TABLE male_first_name (
  name   varchar[20] UNIQUE
);


