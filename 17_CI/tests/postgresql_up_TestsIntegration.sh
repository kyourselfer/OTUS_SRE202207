#!/bin/bash
set +x
export PGDATA=/var/lib/postgresql/11/main
su - postgres -c "ln -s /etc/postgresql/11/main/postgresql.conf $PGDATA/"
su - postgres -c "ln -s /etc/postgresql/11/main/conf.d/ $PGDATA/"
su - postgres -c "ln -s /etc/postgresql/11/main/pg_hba.conf $PGDATA/"
su - postgres -c "/usr/lib/postgresql/11/bin/pg_ctl -D $PGDATA/ start"
su - postgres -c "psql -c 'CREATE DATABASE todo;'"
su - postgres -c "psql -c 'CREATE USER customuser;'"
su - postgres -c "psql -c \"ALTER USER customuser WITH PASSWORD 'custompassword';\""
su - postgres -c "psql -c 'GRANT ALL PRIVILEGES ON DATABASE todo TO customuser;'"
