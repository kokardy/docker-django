#!/bin/sh
echo project name: ${PROJECT_NAME}

sleep 5
############テスト用#######################################
cd ${PROJECT_NAME}
./manage.py runserver 0.0.0.0:8000
###########################################################

############本番用#########################################
# cd ${PROJECT_NAME}
# gunicorn ${PROJECT_NAME}.wsgi:application -b 0.0.0.0:8000
###########################################################

