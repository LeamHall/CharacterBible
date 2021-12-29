-- name:    add_people_db_schemas.sql
-- version: 0.0.1
-- date:    20211227
-- author:  Leam Hall
-- desc:    Create a sample people-y stuff database.

.headers    on
.nullvalue  [NULL]
.echo       on

.read 'data/add_people_data.sql'

.read 'data/add_cultures_data.sql'

.read 'data/add_peopleskills_data.sql'

.read 'data/add_peopleskills_specializations_data.sql'

.read 'data/add_plots_data.sql'

.read 'data/add_political_data.sql'

.read 'data/add_skills_data.sql'

.read 'data/add_specializations_data.sql'

.read 'data/add_temperaments_data.sql'


