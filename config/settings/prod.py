from .base import *

import os
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

ALLOWED_HOSTS += '*'

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Force redirect (helpful on Heroku)
SECURE_SSL_REDIRECT = True

# https://devcenter.heroku.com/articles/sentry#integrating-with-python-or-django
# Viewed with `heroku addons:open sentry`
sentry_sdk.init(
    dsn=os.environ['SENTRY_DSN'],
    integrations=[DjangoIntegration()]
)
