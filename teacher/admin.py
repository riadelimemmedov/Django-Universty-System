from django.contrib import admin


#Django models
from .models import *


#Custom methods
from abstract.admin import TypeUserAdmin

# Register your models here.

admin.site.register(Designation)
admin.site.register(Teacher,TypeUserAdmin)