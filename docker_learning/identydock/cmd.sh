#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server" # development server
  exec python "identydock.py"
else
  echo "Running Production Server" # production server
  exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identydock.py \
             --callable app --stats 0.0.0.0:9191
fi