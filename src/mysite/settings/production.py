'''
base.py is renamed from settings.py after startproject.

Set as follow in manage.py:
DJANGO_SETTINGS_MODULE=mysite.settings.production
'''
from .base import *

# Disable DEBUG during production
DEBUG = False

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = join(dirname(BASE_DIR), 'site', 'static')
