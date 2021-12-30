-- name:    add_people_db_schemas.sql
-- version: 0.0.1
-- date:    20211227
-- author:  Leam Hall
-- desc:    Create a sample people-y stuff databasebase.

.headers    on
.nullvalue  [NULL]
.echo       on


.read 'database/add_cultures_data.sql'

.read 'database/add_peopleskills_data.sql'

.read 'database/add_peopleskills_specializations_data.sql'

.read 'database/add_plots_data.sql'

.read 'database/add_political_data.sql'

.read 'database/add_skill_data.sql'

.read 'database/add_specialization_data.sql'

.read 'database/add_temperament_data.sql'


