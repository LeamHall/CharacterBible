-- name:    add_peopleskills_data.sql
-- version: 0.0.1
-- date:    20201128
-- author:  Leam Hall
-- desc:    Populate sample People/Skill connections.

BEGIN DEFERRED;

INSERT INTO peopleskills (people_id,skill_id,level) VALUES (1,47,1);
INSERT INTO peopleskills (people_id,skill_id,level) VALUES (1,24,1);
INSERT INTO peopleskills (people_id,skill_id,level) VALUES (123,24,1);
INSERT INTO peopleskills (people_id,skill_id,level) VALUES (123,52,1);
INSERT INTO peopleskills (people_id,skill_id,level) VALUES (123,33,2);

END;
