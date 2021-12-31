# CharacterBible

Character parsing, creation, storage, and retrieval.

## Code samples

Database creation in "database/". Sample code in "demo/".

## Requirements

Requires Python 3 and SQLite.

## Usage

./person.py -h
usage: Create, Review, Update, or Delete a person. [-h] [-i IDX] [-c COLUMN] [-l LIKE] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -i IDX, --idx IDX     -i <IDX>
  -c COLUMN, --column COLUMN
                        -c 'last_name'
  -l LIKE, --like LIKE  -l 'Lefron'
  -o OUTPUT, --output OUTPUT
                        -o <text|html>


## Building the initial dataset

  sqlite3 data/people.db < database/write_people_db_schemas.sql

  sqlite3 data/people.db < database/add_people_db_data.sql

  demo/add_people_sample.py



