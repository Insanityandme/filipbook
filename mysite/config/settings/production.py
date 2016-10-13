import dj_database_url
from .base import *  # noqa: F403

# HTTPS

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# Using AWS S3 to store file uploads

# DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
# AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")  # noqa: F405
# AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")  # noqa: F405
# AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")  # noqa: F405

DATABASES["default"] = dj_database_url.config(conn_max_age=600)  # noqa: F405

AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")  # noqa: F405
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")  # noqa: F405
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")  # noqa: F405
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN  # noqa: F405
MEDIA_ROOT = ''  # noqa: F405

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
