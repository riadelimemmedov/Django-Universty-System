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

#Default Sqlite
# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
# }

#Migrate Postgress and Docker
DATABASES = {
        "default": {
            "ENGINE": config("ENGINE"),
            "NAME": config("NAME"),
            "USER": config("USER"),
            "PASSWORD": config("PASSWORD"),
            "HOST": config("HOST",'127.0.0.1'),
            "PORT": config('PORT',5432)
        }
    }

#!Installed Apps
INSTALLED_APPS += []


#!Middleware
MIDDLEWARE += []

"""
These commented config will use when you are runnning the project on Docker
"""
