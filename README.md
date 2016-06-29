# django-proj-template
Preparing starting point quickly for a new Django project. This provides the
facility for prototyping (Mockup) of your web pages using TemplateView.

Creating Mockup is not going to be a waste of time using this.

## Quick start
After cloning this repo, prepare your development environment.

Assuming you have Python3.4 installed. Use separate virtualenv directory:

    $ virtualenv -p python3.4  ~/.envs/<proj_name>
    $ source ~/.envs/<proj_name>/bin/activate

Install all dependencies:

    $ pip install -r requirements.txt

Create new local git branch for your project and run migrations:

    $ git checkout -b <project_name>
    $ git migrations

Initial test, localhost:8000/index.html:

    $ python manage.py runserver

