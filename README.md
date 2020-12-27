# gita-sql

### Use SQLITE3, MySQL / MariaDB or Postgres
### Will be adding Nosql databases also in future

* folder sql
* start with gita_intro.sql
* continue with gita.sql
* update with gitaupdate1.sql
* update with gitaupdate2.sql
* optional try upanishad.sql

```
$ sqlite3 gita.db
sqlite> .read <filename>

sqlite> .read gita_intro.sql
sqlite> .read gita.sql
sqlite> .read gitaupdate1.sql
sqlite> .read gitaupdate2.sql
sqlite> .read upanishad.sql
```

### To build the python-flask software
### You will need docker and docker-compose installed
### Please ensure you fix the install folder in Makefile
```
# cleanup
make cleanup
# build
make build
# prune
make prune
```

### Copyright Dev Bhattacharyya