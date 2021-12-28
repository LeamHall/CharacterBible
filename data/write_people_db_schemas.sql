-- name:    write_people_db_schemas.sql
-- version: 0.0.1
-- date:    20211227
-- author:  Leam Hall
-- desc:    Create a sample people-y stuff database.

.headers    on
.nullvalue  [NULL]
.echo       on

.read 'data/write_people_table.sql'

.read 'data/write_cultures_table.sql'

.read 'data/write_peopleskills_table.sql'

.read 'data/write_peopleskills_specializations_table.sql'

.read 'data/write_plots_table.sql'

.read 'data/write_political_table.sql'

.read 'data/write_skills_table.sql'

.read 'data/write_specializations_table.sql'

.read 'data/write_temperaments_table.sql'


