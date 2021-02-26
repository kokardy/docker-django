#!/bin/sh
sleep 10

./${PROJECT_NAME}/manage.py runserver 0.0.0.0:8000
#gunicorn ${PROJECT_NAME}.wsgi -b 0.0.0.0:8000

