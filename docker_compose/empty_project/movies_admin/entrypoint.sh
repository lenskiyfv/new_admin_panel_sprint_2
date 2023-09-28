#!/bin/sh

sleep 1

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput

uwsgi --strict --ini uwsgi.ini

exec "$@"