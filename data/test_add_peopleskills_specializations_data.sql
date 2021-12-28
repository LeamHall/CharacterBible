-- name:    test_add_peopleskills_specializations.sql
-- version  0.0.1
-- date:    20211228
-- author:  Leam Hall
-- desc:    Populate Test Culture table.

BEGIN DEFERRED;

INSERT INTO peopleskills_specializations (people_id, skill_id, specialization_id, level) VALUES (1,24,1,1);

END;
