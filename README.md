# CharacterBible

Character parsing, creation, storage, and retrieval.

## Code samples

Database creation in "database/". Sample code in "demo/".

## Requirements

Requires Python 3 and SQLite.

## Usage

```
./character_bible.py -h
```

## Admin tool

```
./cb_admin.py -h
```

## Building the initial dataset

```
  sqlite3 data/people.db < database/write_people_db_schemas.sql

  sqlite3 data/people.db < database/add_people_db_data.sql

  demo/add_people_sample.py
```


