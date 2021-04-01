import os
if os.environ.get('DJANGO_SETTINGS_MODULE') == 'aboleyn.settings.production':
    from .production import *
else:
    from .development import *
