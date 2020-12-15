# Coursework 
## Callboard 

This repository contains a backend and frontend for callboard. 

### Used technologies
- [Django REST Framework](https://www.django-rest-framework.org/);
- [Vue js](https://vuejs.org/);
- Additional libraries for this technologies ([corsheaders](https://pypi.org/project/django-cors-headers/), [djoser](https://djoser.readthedocs.io/en/latest/getting_started.html), [allauth](https://django-allauth.readthedocs.io/en/latest/installation.html), [jquery](https://jquery.com/), [bootstrap](https://getbootstrap.com/), [popper](https://github.com/RobinCK/vue-popper) etc.).

### Pre Requirements
- [Python](https://www.python.org/downloads/release/python-380/) 3.8 or higher;
- [Node js](https://nodejs.org/uk/);

### Start backend
```
pipenv install
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
    Username 
    Password
    Password again
pipenv run python manage.py loaddata ./import_data/filters.json
pipenv run python manage.py loaddata ./import_data/categories.json
pipenv run python manage.py loaddata ./import_data/terms.json
pipenv run python manage.py runserver
```
- To check launch backend go to the link:
```
http://127.0.0.1:8000/
```

### Start frontend
```
cd frontend/callboard-front/
npm install
npm run serve
```

- To check launch frontend go to the link:
```
http://localhost:8080/
```