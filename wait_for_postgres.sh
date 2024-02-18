#!/bin/bash

check_postgres() {
    until pg_isready -h localhost -p 5432 -U postgres
    do
        echo "Waiting for PostgreSQL to start..."
        sleep 1
    done
    sleep 5
    echo "PostgreSQL is ready!"
}

check_postgres

exec "$@"
