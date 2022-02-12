-- name:    test_add_people_skill_level_data.sql
-- version: 0.0.1
-- date:    20220212
-- author:  Leam Hall
-- desc:    Populate test sample People/Skill connections.

BEGIN DEFERRED;

INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (2, 1, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (2, 2, 1);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (2, 3, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (3, 2, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (3, 4, 2);
INSERT INTO people_skill_level (people_idx, skill_idx, skill_level) VALUES (3, 5, 1);

END;
