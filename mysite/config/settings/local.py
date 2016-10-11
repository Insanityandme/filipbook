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

INSTALLED_APPS += ("debug_toolbar", )
debug_toolbar = 'debug_toolbar.middleware.DebugToolbarMiddleware'
MIDDLEWARE.insert(0, debug_toolbar)
