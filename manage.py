#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # :NOTE:
    # - Change environment to Production for public website
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "mysite.settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
