
DROP TABLE IF EXISTS skill_list;
CREATE TABLE skill_list (
  idx INTEGER PRIMARY KEY,
  skill TEXT
) ;

INSERT INTO skill_list (skill) VALUES ('CbtR');
INSERT INTO skill_list (skill) VALUES ('Kissing');
INSERT INTO skill_list (skill) VALUES ('Blade');
INSERT INTO skill_list (skill) VALUES ('Lockpicking');
INSERT INTO skill_list (skill) VALUES ('Stealth');

DROP TABLE IF EXISTS people;
CREATE TABLE people (
  idx INTEGER PRIMARY KEY,
  f_name TEXT,
  l_name TEXT
);

INSERT INTO people (f_name, l_name) VALUES ('Jakob', 'Domici');
INSERT INTO people (f_name, l_name) VALUES ('Liv', 'Ellis');

DROP TABLE IF EXISTS people_skill_level;
CREATE TABLE people_skill_level (
  idx INTEGER PRIMARY KEY,
  people_idx INTEGER NOT NULL REFERENCES people(idx),
  skill_idx INTEGER NOT NULL REFERENCES skill_list(idx),
  skill_level INTEGER NOT NULL 
);

INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (1, 1, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (1, 2, 1);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (1, 3, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (2, 2, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (2, 4, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (2, 5, 1);

