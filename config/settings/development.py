from ..base import *
from decouple import config

#!Debug
DEBUG = True

#!Allowed Hosts
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

#!Databases
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
}

#!Installed Apps
INSTALLED_APPS += []


#!Middleware
MIDDLEWARE += []

"""
These commented config will use when you are runnning the project on Docker
"""
