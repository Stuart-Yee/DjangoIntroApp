# DjangoIntroApp
Introduction to Django

Part I March 12th 2023
Creating a new Project and App

1) Start a virtual environment of your choice
2) If using GitHub, select "Python" for your .gitignore
3) Install Django `pip install django`
4) Create project `django-admin startproject {project name}`
5) In new project folder, create a new package (folder with `__init__.py`) called "apps"
6) Navigate into the apps folder and create a new app - `../manage.py startapp {app name}`
7) Navigate into the new {app name} directory, open `apps.py` and change name to `app.s{app name}`
8) Open `settings.py` within the {project name} directory and add app to the `INSTALLED_APPS` list as `"apps.{app name}"`
9) Migrate - `python manage.py makemigrations` and then `python manage.py migrate`
10) Test the server `python manage.py runserver`

Creating a Superuser and Logging In
1) Enter `python manage.py createsuperuser` and follow prompts
2) Login at `http://localhost:8000/admin`

Set up routing with urls.py
1) Create `urls.py` in {app name} directory
2) Go to project level `urls.py` in `{project name}/{project name}/urls.py`

Setting up Templates and Static
1) In your {app name} directory create a `satic` and `templates`

