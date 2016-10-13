from .base import *  # noqa: F403

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite_db',
        'USER': 'insanityandme',
        'PASSWORD': 'crankelton4458',
    }
}

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']  # noqa: F405

INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
debug_toolbar = 'debug_toolbar.middleware.DebugToolbarMiddleware'
MIDDLEWARE.insert(0, debug_toolbar)  # noqa: F405
