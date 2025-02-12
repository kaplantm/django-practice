Reference: https://www.youtube.com/watch?v=Rp5vd34d-z4

# Lesson 1
## Python version
Python 3.12.8
pip 25.0.1
Django 5.1.6

## Venv
python -m venv .venv
. .venv/bin/activate
python -m pip install Django

## Creating a Django Project
django-admin startproject myproject

## Running the project
cd myproject
python manage.py runserver # runs on port 8000 by default

# Lesson 2

## Creating a Django App
Apps should be module, we might have different parts of a larger project broken into apps. Today we're going to create an app for posts but you could also have an app for users or tasks or shopping cart, anything you might break out into separate features. And they're modular - you might be able to take an an app from one Django project and put in in another. You've breaking out the logic into apps that can work independently.

python manage.py startapp posts