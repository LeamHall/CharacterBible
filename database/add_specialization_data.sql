-- name:    add_specialization_data.sql
-- version: 0.0.1
-- date:    20201128
-- author:  Leam Hall
-- desc:    Populate the specializations table.

BEGIN DEFERRED;

INSERT INTO specializations (specialization) VALUES ('CbtR');
INSERT INTO specializations (specialization) VALUES ('HvyWpn');
INSERT INTO specializations (specialization) VALUES ('Wheeled');
INSERT INTO specializations (specialization) VALUES ('HTH');
INSERT INTO specializations (specialization) VALUES ('Blade');



END;

