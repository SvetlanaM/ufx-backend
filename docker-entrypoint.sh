#!/bin/bash

#database migrations
python3 manage.py migrate
python3 manage.py createsuperuser
#collect static files
python3 manage.py collectstatic --noinput


# Prepare log files and start outputting logs to stdout
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &


# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn ufx.wsgi:application \
    --name ufx_devel \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    "$@"
