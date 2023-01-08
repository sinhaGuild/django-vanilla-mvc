# Django Recipe

# Project Setup

## Init and run migrations Migrations
```sh
# make migrations
python3 -m manage.py makemigration books
# check sql code generated
python3 -m manage.py sqlmigrate books 0001
# apply migrations
python3 -m manage.py migrate
```
## Run Server
```sh
python3 -m manage.py runserver
```

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .tables (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.

### Modify Models
Each model is represented by a class that subclasses django.db.models.Model. 
Plug Config object from apps.py into main/settings.py

# Modify Routes
Create a new `view` function, and a new route in `urls`. This should reference a template file in `books/templates/books/...`