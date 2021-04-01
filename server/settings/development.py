import logging
logging.basicConfig(level=logging.DEBUG)

from .base import *

DEBUG = True
logging.info('DEBUG: %s'%DEBUG)
logging.info('BASE_DIR: %s'%BASE_DIR)

# Allowed hosts

ALLOWED_HOSTS = ['*']
logging.info('ALLOWED_HOSTS: %s'%str(ALLOWED_HOSTS))
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

logging.info('INSTALLED_APPS: %s'%str(INSTALLED_APPS))

MIDDLEWARE = [ # https://docs.djangoproject.com/en/3.1/ref/middleware/
    #'django.middleware.security.SecurityMiddleware', # Provides several security enhancements to the request/response cycle.
    #'whitenoise.middleware.WhiteNoiseMiddleware', # Serve static files in production, not used in developemnet
    'django.contrib.sessions.middleware.SessionMiddleware', # Enables session support.
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # Among other things, forbids access to user agents in the DISALLOWED_USER_AGENTS setting.
    #'django.middleware.csrf.CsrfViewMiddleware', # Adds protection against Cross Site Request Forgeries by adding hidden form fields.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Adds the user attribute, representing the currently-logged-in user, to every incoming HttpRequest object.
    'django.contrib.messages.middleware.MessageMiddleware', # Enables cookie- and session-based message support.
    #'django.middleware.clickjacking.XFrameOptionsMiddleware', # Simple clickjacking protection via the X-Frame-Options header.
    #'TokenMiddleware.TokenMiddleware', # Verify access token
]
logging.info('MIDDLEWARE: %s'%str(MIDDLEWARE))

# Testing

TEST_RUNNER = 'server.tests.DiscoverRunnerNoDatabase' # This allows us to run tests without creating a new test db

# Extra places for static files
STATICFILES_DIRS = [
    Path(BASE_DIR).resolve() / 'ui'
] # Where the files are copied from...
logging.info('STATICFILES_DIRS: %s'%str(STATICFILES_DIRS))

