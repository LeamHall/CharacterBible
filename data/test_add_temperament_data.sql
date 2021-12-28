-- name:    test_add_temperament_data.sql
-- version  0.0.1
-- date:    20211228
-- author:  Leam Hall
-- desc:    Populate Test Temperament table.

BEGIN DEFERRED;
INSERT INTO temperaments (temperament) VALUES ( 'Crafter' );
END;
