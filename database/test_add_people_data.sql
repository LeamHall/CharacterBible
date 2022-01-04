-- name:    add_people_data.sql 
-- version: 0.0.1
-- date:    20211228
-- author:  Leam Hall
-- desc:    Populate people stuff database.

BEGIN DEFERRED;

INSERT INTO people ( last_name, first_name, middle_name, gender, birthdate, plot, temperament, notes) VALUES ( "Romero", "Cecil", NULL, "m", 1413242, NULL, NULL, "" );

END;

