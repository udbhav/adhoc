#!/bin/sh
# Remember that this script will be executed by the unix user who push to the
# git repository ; and the script will be executed in ~/www/codebase/.

# Update requirements
. /home/udbhav/adhoc-env/bin/activate
pip install -r ~/www/django/adhoc/requirements.txt
python ~/www/django/adhoc/manage.py collectstatic --noinput
