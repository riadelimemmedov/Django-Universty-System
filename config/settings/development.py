from ..base import *
from decouple import config

#!Debug
DEBUG = True


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
            "NAME": config("POSTGRES_DB"),
            "USER": config("POSTGRES_USER"),
            "PASSWORD": config("POSTGRES_PASSWORD"),
            "HOST": config("POSTGRES_HOST"),
            "PORT": config('POSTGRES_PORT',5432)
        }
    }

#!Installed Apps
INSTALLED_APPS += []


#!Middleware
MIDDLEWARE += []

"""
These commented config will use when you are runnning the project on Docker
"""
