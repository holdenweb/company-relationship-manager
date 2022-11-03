#!/bin/bash
docker-compose run -w "/app/crm" api pipenv run pytest