#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

Useful commands:

python manage.py help <subcommand>
python manage.py check

python manage.py runserver --noreload localhost:8000
python manage.py runserver --noreload 0.0.0.0:8000 # For access on local network
python manage.py runsslserver --noreload localhost:8000
python manage.py runsslserver --noreload 0.0.0.0:8000 # For secure access on local network

python manage.py shell


"""
import os
import sys


def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?") from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
