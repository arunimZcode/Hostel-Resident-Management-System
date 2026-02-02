#!/bin/sh
set -e

# Apply database migrations and collect static files, then start Gunicorn
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn hostel_hms.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3
