# My first project using django.

### 1. Environment
    Anaconda, Pycharm, Emacs(My favorite)

### 2. Initial Install Step
    1-1. Meke project in pycharm, virtual env.
    1-2. Install django, start project. (i use conda env)
    
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


# For cloud server setting
### 1. Check insall Python
### 2. Virtual Evn setting
    2-1. Visit Anaconda.com/downloads
    2-2. Copy the bash installer link
    2-3. User wget to download the bash installer
    2-4. Run bash script to install Anaconda3
    2-5. conda create -n django python
    2-6. install prerequisite library in virtual env. (before "no such table" error is shown)
    2-7. python manage.py makemigrations
    2-8. python manage.py migrate

3. IP address connect
