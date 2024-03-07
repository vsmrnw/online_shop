from .base import *

DEBUG = False
ADMINS = [
    env.tuple('ADMINS'),
]
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
    }
}
