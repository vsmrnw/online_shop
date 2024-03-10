from .base import *

DEBUG = False
ADMINS = [
    env.tuple('ADMINS'),
]
ALLOWED_HOSTS = ['online-shopproject.com', 'www.online-shopproject.com']

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

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
