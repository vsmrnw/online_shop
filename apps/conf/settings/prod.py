from .base import *

DEBUG = False
ADMINS = [
    env.tuple('ADMINS'),
]
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASS'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
