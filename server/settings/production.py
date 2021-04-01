import logging
logging.basicConfig(level=logging.DEBUG)

from .base import *

DEBUG = False
logging.info('DEBUG: %s'%DEBUG)
logging.info('BASE_DIR: %s'%BASE_DIR)

# Environment settings

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Allowed hosts

ALLOWED_HOSTS = ['*'] # Prod domain name needs to be set here!
logging.info('ALLOWED_HOSTS: %s'%str(ALLOWED_HOSTS))
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

logging.info('INSTALLED_APPS: %s'%str(INSTALLED_APPS))

MIDDLEWARE = [ # https://docs.djangoproject.com/en/3.1/ref/middleware/
    'django.middleware.security.SecurityMiddleware', # Provides several security enhancements to the request/response cycle.
    'whitenoise.middleware.WhiteNoiseMiddleware', # Serve static files in production, not used in developemnet
    'django.contrib.sessions.middleware.SessionMiddleware', # Enables session support.
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # Among other things, forbids access to user agents in the DISALLOWED_USER_AGENTS setting.
    #'django.middleware.csrf.CsrfViewMiddleware', # Adds protection against Cross Site Request Forgeries by adding hidden form fields.
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Adds the user attribute, representing the currently-logged-in user, to every incoming HttpRequest object.
    'django.contrib.messages.middleware.MessageMiddleware', # Enables cookie- and session-based message support.
    #'django.middleware.clickjacking.XFrameOptionsMiddleware', # Simple clickjacking protection via the X-Frame-Options header.
    'TokenMiddleware.TokenMiddleware', # Verify access token
]
logging.info('MIDDLEWARE: %s'%str(MIDDLEWARE))

STATIC_ROOT = Path(BASE_DIR).resolve() / 'ui'
logging.info('STATIC_ROOT: %s'%str(STATIC_ROOT))

