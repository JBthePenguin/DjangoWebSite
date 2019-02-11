# Strucure of a Django Web Site
**A structure of a Web site with a presentation, a portfolio, a blog, a contact page and using the frameworks [Django](https://www.djangoproject.com/), [Bootstrap4](https://getbootstrap.com/), [jQuery](https://jquery.com/).
So, to install and use it :**
## Create a PostgreSQL database for the application and a new user
*!!! maybe you have to install [PostgreSQL](https://www.postgresql.org/) !!!*
Connect to PostgreSQL client, create database and new user with privileges:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# CREATE USER "djangowebsite";
postgres=# ALTER USER djangowebsite WITH PASSWORD 'cool';
postgres=# CREATE DATABASE "db_djangowebsite";
postgres=# GRANT ALL PRIVILEGES ON DATABASE db_djangowebsite TO djangowebsite;
postgres=# \q
postgres@somewhere:~$ exit
```
## Clone the application and install the necessary requirements
Clone the folder, go inside, create a virtual environment for Python with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*), use it, and install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [psycopg2](https://github.com/psycopg/psycopg2), [psycopg2-binary](https://pypi.org/project/psycopg2-binary/):
```shell
$ git clone https://github.com/JBthePenguin/DjangoWebSite.git
$ cd DjangoWebSite
$ virtualenv -p python3 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
## Create tables
Make the migrations:
```shell
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
## Admin site
Create a "superuser" account:
```shell
(env)$ python manage.py createsuperuser
```
## Start and use the Application
```shell
(env)$ python manage.py runserver
```
**NOW, with your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the application and [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) for the admin site.**
