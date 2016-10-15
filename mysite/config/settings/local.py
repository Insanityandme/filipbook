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


def show_toolbar(request):
    return True

# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html
# http://stackoverflow.com/questions/9566676/django-debug-toolbar-in-heroku
# Ensures that the debug_toolbar can be shown on my staging server

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'config.settings.local.show_toolbar'
}
