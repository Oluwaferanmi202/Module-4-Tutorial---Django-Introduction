
python -m venv .venv
.venv\Scripts\activate
pip install django
django-admin startproject mysite
cd mysite
python manage.py startapp myapp
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver