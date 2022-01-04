-- name:    add_peopleskills_specializations_data.sql
-- version: 0.0.1
-- date:    20201128
-- author:  Leam Hall
-- desc:    Populate sample People/Skill connections.

BEGIN DEFERRED;

INSERT INTO peopleskills_specializations (people_id, skill_id, specialization_id, level) VALUES (1,1,1,1);

END;
