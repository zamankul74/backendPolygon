# Project used

# PostgreSQL
# db name: poligon ( not polygon :) )
# with user same as in settings.py
# to create poligon db
sudo -u postgres psql
# Django 3.6.x
# instaled extantions:

# install django-postgres
# install rest_framework
# install djangorestframework django-cors-headers
# install build-dep python-psycopg
# install psycopg2-binary
# install postgresql postgresql-contrib

# server work on default port
# not used session auth for client requests

# DB migration
python manage.py makemigrations todo
python manage.py migrate

# python manage.py createsuperuser --username=slava --email=zamankul_74@yahoo.com

# RUN server

python manage.py runserver
