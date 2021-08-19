## NOTE

#### Part-1: Basic setup

1. python -m venv . : Create the vertual environment
2. .\Scripts\activate : Activate the virtual environment
3. pip freeze > requirements.txt : Create the requirements.txt file(first empty)
4. pip install "django>=3.2,<4.0" : Install the django package between version 3.2 and 4.0 (Version specified for production)
5. Create TODO to be clear with your vision.
6. Create the src folder in which we create our app.cd src - go inside src
7. django-admin startproject djangoflix . : create new django project

#### Part-2: Video Player
- Create a new app called video
- Create video model in video app.
- Register app and put it in installed all, then make the migration also run tests.(python manage.py test videos)
- create a new superuser

- **Test-1** 
- In video app -> test -> create a new test

#### Part-3: Add app in admin also create proxys
- In video app -> admin.py -> add app to admin
- Added model proxys in admin.py
---

## OPTIONAL:

1. python -m pip install --upgrade pip : Upgrade the pip package in venv
