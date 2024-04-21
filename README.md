# Admin panel for avito intagration

## Requirements
1. python >= 3.0

## Installation
1. ```git clone``` this project
2. ```python -m venv venv```
3. ```source venv/bin/activate```
4. ```pip install -r requirements.txt```
5. ```python manage.py makemigrations && python manage.py migrate``` for database set up
6. ```python manage.py createsuperuser``` for admin user seeding (you cannot register admin)
7. ```python manage.py runserver``` for local usage