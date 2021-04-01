#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.

Useful commands:

python server\manage.py help <subcommand>
python server\manage.py check

python server\manage.py runserver --noreload localhost:8000
python server\manage.py runserver --noreload 0.0.0.0:8000 # For access on local network
python server\manage.py runsslserver --noreload localhost:8000
python server\manage.py runsslserver --noreload 0.0.0.0:8000 # For secure access on local network

python server\manage.py shell


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
