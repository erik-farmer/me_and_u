from .base import *

import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# copy-pasta from: https://devcenter.heroku.com/articles/django-assets
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE += 'whitenoise.middleware.WhiteNoiseMiddleware'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
