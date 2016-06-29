# django-proj-template
Quick preparation for a new Django project. Generating Mockups for new webpages is easy with TemplateView.

Simply create html file in *templates* directory. Django template can be used during the prototyping. No waste of time.

## Quick start
After cloning this repo, prepare your development environment.

Assuming you have Python3.4 installed. Use separate virtualenv directory:

    $ virtualenv -p python3.4  ~/.envs/<proj_name>
    $ source ~/.envs/<proj_name>/bin/activate

Install all dependencies:

    $ pip install -r requirements.txt

Create new local git branch for your project and run migrations:

    $ git checkout -b <project_name>
    $ python manage.py migrate

Initial test, localhost:8000/index.html:

    $ python manage.py runserver

