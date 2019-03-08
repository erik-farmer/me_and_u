from .base import *

import os
import dj_database_url

ALLOWED_HOSTS += '*'

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
