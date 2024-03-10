# Text to HTML generator

## Description

**Here you can convert the text and title of the future page into HTML page code, for this you need to log in**

## Technologies used in the project
- Python
- Django
- Postgresql
- Docker
- Docker-compose
- Git

## Local setup

**Create python environment**

```
$ python3 -m venv venv
```

**Activate python environment**

```
$ source venv/bin/activate
```

**Install dependencies**

```
$ pip install -r requirements.txt
```

**Create .env file and insert there all code from .envexample file**

```
$ touch .env
```

**Build web and database containers**

```
$ sudo docker-compose build
```

**Run web and database containers**

```
$ sudo docker-compose up
```

**Go to the middle of the running container in a new terminal window**

```
$ sudo docker-compose exec web bash
```

**Perform database migrations**

```
$ python manage.py migrate
```

**Create superuser**

```
$ python manage.py createsuperuser
```