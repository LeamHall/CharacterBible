-- name:    test_add_culture_data.sql
-- version  0.0.1
-- date:    20211228
-- author:  Leam Hall
-- desc:    Populate Test Culture table.

BEGIN DEFERRED;
INSERT INTO cultures (id, culture) VALUES ( 1, 'Clan' );
END;
