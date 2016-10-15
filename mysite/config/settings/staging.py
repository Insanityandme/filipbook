import dj_database_url
from .base import *  # noqa: F403

DEBUG = True

ALLOWED_HOSTS += ['filipbook-staging.herokuapp.com']  # noqa: F405

INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
debug_toolbar = 'debug_toolbar.middleware.DebugToolbarMiddleware'
MIDDLEWARE.insert(0, debug_toolbar)  # noqa: F405

DATABASES["default"] = dj_database_url.config(conn_max_age=600)  # noqa: F405
