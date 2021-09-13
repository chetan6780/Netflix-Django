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

#### Part-4: Increasing models
- Add publish timestamp
- Write test for publish timestamp
- Make and test slugify , here we use video_id as unique so we don't really need slugify.
- Added custom model manager and custom queryset
- Deleted custom save method and used pre_save signal
---

#### Part-5: Playlist
- Created new app for playlists
- Register app in settings.py
- Created test for playlists
- Added app in admin.py
- Used Django-Managed Python Shell to explore Foreign Keys
- used django shell to see actual action


#### Part-6: Many To Many Foreign Keys
- creating many-to-many foreign keys with related name and test them.
- Created Tabular Inline in the admin Many To Many feilds
- Updated Tests for Through Model

### Part-7: Playlists (Seasons)

## OPTIONAL:

1. python -m pip install --upgrade pip : Upgrade the pip package in venv
