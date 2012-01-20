#!/bin/sh
. /home/udbhav/adhoc-env/bin/activate
pip install -r ~/www/django/adhoc/requirements.txt
python ~/www/django/adhoc/manage.py collectstatic --noinput
