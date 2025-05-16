#!/bin/bash
# Release script for deployment
export $(grep -v '^#' .env | xargs) 2>/dev/null
python manage.py collectstatic --noinput
echo "Static files collected. Ready for deployment."
