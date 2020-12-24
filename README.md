# My first project using django.

### 1. Environment
    Anaconda, Pycharm, Emacs(My favorite)

### 2. Initial Install Step
    1-1. Meke project in pycharm, virtual env.
    1-2. Install django, start project. (in virtual
    
        django-admin startproject 

    1-3. Migrate -> Create sqlite (add gitignore)

       python manage.py

    1-4. Run server.

       python manage.py runserver


    Then, You can see the first django page!
    Access 127.0.0.1:8000

    1-5. Start App
         python manage.py startapp blogapp
    (every step, take care about commit necessary files and exclude unnecessary files in .gitignore (ex. sqlite, migrations)


python manage.py createsuperuser
python manage.py runserver (check admin page)
python manage.py makemigrations (specify isntalled blogapp in setting page)
python manage.py migrate (reflect the change)