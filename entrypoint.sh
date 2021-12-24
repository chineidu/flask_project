#! /bin/sh

echo "waiting for postgres..."

while ! nc -z api-db 5432; do
    sleep 0.10
done

echo "PostgreSQL has started"

python manage.py run -h 0.0.0.0
