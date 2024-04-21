# Admin panel for avito intagration

## Requirements
1. python >= 3.0

## Installation
1. ```git clone``` this project
2. ```python -m venv venv```
3. ```source venv/bin/activate```
4. ```pip install -r requirements.txt```
5. Run ```cp .env.example .env``` and fill ```.env``` with your data
6. ```python manage.py makemigrations && python manage.py migrate``` for database set up
7. ```python manage.py createsuperuser``` for admin user seeding (you cannot register admin)
8. ```python manage.py runserver``` for local usage