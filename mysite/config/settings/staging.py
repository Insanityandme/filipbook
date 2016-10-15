import dj_database_url
from .base import *  # noqa: F403

DEBUG = True

ALLOWED_HOSTS += ['filipbook-staging.herokuapp.com']  # noqa: F405

DATABASES["default"] = dj_database_url.config(conn_max_age=600)  # noqa: F405
