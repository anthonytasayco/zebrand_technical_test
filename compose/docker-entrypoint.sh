#!/bin/bash

echo "Apply migrations"
python ./source/manage.py migrate --settings=config.settings.local

echo "Starting server"
python ./source/manage.py runserver 0.0.0.0:8000 --settings=config.settings.local