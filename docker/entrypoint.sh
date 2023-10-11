#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -e

pip install --user --no-cache-dir -U packaging mysqlclient
pip install --user --no-cache-dir -U -r requirements.txt

python manage.py migrate

# https://stackoverflow.com/questions/32255814/what-purpose-does-using-exec-in-docker-entrypoint-scripts-serve/32261019#32261019
exec "$@"
