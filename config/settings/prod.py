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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "me_and_u" / "static",
]
STATIC_ROOT = BASE_DIR / 'static_root'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
