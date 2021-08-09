Project Polygon Backend

PostgreSQL
db name: poligon ( not polygon :) )
with user same as in settings.py

To create poligon db
### `sudo -u postgres psql`
Django 3.6.x
instaled extantions:

django-postgres
rest_framework
djangorestframework django-cors-headers
build-dep python-psycopg
psycopg2-binary
postgresql postgresql-contrib

Server work on default port
Note: not used session auth for client requests

DB migration
### `python manage.py makemigrations todo`
### `python manage.py migrate`

### `python manage.py createsuperuser --username=slava --email=<any email>`

RUN server

### `python manage.py runserver`
