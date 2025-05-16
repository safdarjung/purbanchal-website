#!/bin/bash
# Run the Django development server
export $(grep -v '^#' .env | xargs) 2>/dev/null
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
