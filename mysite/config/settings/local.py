from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite_db',
        'USER': 'insanityandme',
        'PASSWORD': 'crankelton4458',
    }
}

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
INSTALLED_APPS += ["debug_toolbar"]
debug_toolbar = 'debug_toolbar.middleware.DebugToolbarMiddleware'
MIDDLEWARE.insert(0, debug_toolbar)

MEDIA_ROOT = BASE_DIR.child("media")
