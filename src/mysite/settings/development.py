'''
base.py is renamed from settings.py after startproject.
'''
from .base import *

# Enable DEBUG during development
DEBUG = True

# Show emails to console in DEBUG mode
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
