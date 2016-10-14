import dj_database_url
from .base import *  # noqa: F403

# HTTPS

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

DATABASES["default"] = dj_database_url.config(conn_max_age=600)  # noqa: F405
