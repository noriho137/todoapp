# ToDoApp

ToDoApp is a task management application.
Note that this application supports Japanese only.


## Requirements

* OS: Windows10 Pro (It will probably also work with Linux, but has not been tested yet.)
* Python 3.8


## Installation

```bash
$ git clone https://github.com/noriho137/todoapp.git
$ cd todoapp/
$ python -m venv {venv_name}
$ {venv_name}/Scripts/activate.bat
({venv_name}) $ pip install -r requirements.txt
```


## Set up environment variables

Generate Django secret key by ```secrets.token_urlsafe```.

```bash
({venv_name})$ python -c "import secrets; print(secrets.token_urlsafe(38))"
```

Make ```.env``` file at project root directory and define environment variables like following:

```bash
# Django settings
export DJANGO_SECRET_KEY={Django secret key generated above}
export DJANGO_DEBUG=True
```


## Migration

```bash
({venv_name})$ python manage.py makemigrations
({venv_name})$ python manage.py migrate
```


## How to run

```bash
({venv_name})$ python manage.py runserver
```

Browse to http://127.0.0.1:8000/ .
