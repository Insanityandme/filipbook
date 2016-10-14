import dj_database_url
from .base import *  # noqa: F403

# HTTPS

CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False

SECURE_SSL_REDIRECT = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False

DATABASES["default"] = dj_database_url.config(conn_max_age=600)  # noqa: F405
