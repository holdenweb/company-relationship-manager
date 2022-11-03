#!/bin/bash
docker-compose up -d db
docker-compose run api ./crm/manage.py migrate
docker-compose up