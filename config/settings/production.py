from ..base import *
from decouple import config

#!Debug
DEBUG = False

#!Allowed Hosts
ALLOWED_HOSTS = [
    #'Your Production Hosts Adress'
]


#!DATABASES
#?Not Touch this line,because not configutation docker image,use only local
# DATABASES = {
#     "default": {
#       Using docker postgres image
#     }
# }