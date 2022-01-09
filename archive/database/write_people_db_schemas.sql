-- name:    write_people_db_schemas.sql
-- version: 0.0.1
-- date:    20211227
-- author:  Leam Hall
-- desc:    Create a sample people-y stuff databasebase.

.headers    on
.nullvalue  [NULL]
.echo       on

.read 'database/write_people_table.sql'

.read 'database/write_cultures_table.sql'

.read 'database/write_peopleskills_table.sql'

.read 'database/write_peopleskills_specializations_table.sql'

.read 'database/write_plots_table.sql'

.read 'database/write_political_table.sql'

.read 'database/write_skills_table.sql'

.read 'database/write_specializations_table.sql'

.read 'database/write_temperaments_table.sql'


