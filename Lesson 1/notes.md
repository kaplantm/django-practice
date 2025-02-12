# Python version
Python 3.12.8
pip 25.0.1
Django 5.1.6

# Venv
python -m venv .venv
. .venv/bin/activate
python -m pip install Django

# Django
django-admin startproject myproject
cd myproject
python manage.py runserver # runs on port 8000 by default
