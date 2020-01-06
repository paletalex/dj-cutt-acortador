from .base import *

DEBUG = False

ALLOWED_HOSTS = ['cuttt.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcovo3j91bdgif',
        'USER': 'puhhzlkwgktqzm',
        'PASSWORD': '6e06d660a342f62993a8802047fcc6b4d168773eac2b3dbd97320aab30017e82',
        'HOST': 'ec2-174-129-33-13.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')