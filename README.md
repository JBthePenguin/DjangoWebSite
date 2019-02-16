## Strucure of a Django Web Site [![Build Status](https://travis-ci.com/JBthePenguin/DjangoWebSite.svg?branch=master)](https://travis-ci.com/JBthePenguin/DjangoWebSite)
**A structure of a Web site with a presentation, a portfolio, a blog, a contact page and using the frameworks [Django](https://www.djangoproject.com/), [Bootstrap 4](https://getbootstrap.com/), [jQuery](https://jquery.com/).
So, to install and use it :**
### Create a PostgreSQL database for the application and a new user
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
### Clone the application and install the necessary requirements
Clone the folder, go inside, create a virtual environment for Python with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*), use it, and install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [django-fixture-magic](https://github.com/davedash/django-fixture-magic), [future](https://pypi.org/project/future/), [psycopg2](https://github.com/psycopg/psycopg2), [psycopg2-binary](https://pypi.org/project/psycopg2-binary/), [Pillow](https://pillow.readthedocs.io/en/stable/), [selenium](https://selenium-python.readthedocs.io/)):
```shell
$ git clone https://github.com/JBthePenguin/DjangoWebSite.git
$ cd DjangoWebSite
$ virtualenv -p python3 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
### Create tables
Make the migrations:
```shell
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
### Admin site
Create a "superuser" account:
```shell
(env)$ python manage.py createsuperuser
```
### Start and use the Application
```shell
(env)$ python manage.py runserver
```
**NOW, with your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the application and [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin) for the admin site where you can add categories and projects in portfolio.**
### Tests
The tests use [selenium](https://selenium-python.readthedocs.io/) and maybe you have to install [GreckoWebdriver](https://github.com/mozilla/geckodriver/releases) to use firefox.
During the tests, a temporary database is creating, so you need to update the role of application:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# ALTER USER djangowebsite CREATEDB;
postgres=# \q
postgres@somewhere:~$ exit
```
Run the tests:
```shell 
(env)$ python manage.py test -v 2
```
If you want to use Chrome, install [ChromeWebDriver](http://chromedriver.chromium.org/downloads) and update in websiteapp/browser_selenium.py line 2:
```python
from selenium.webdriver.chrome.webdriver import WebDriver
```