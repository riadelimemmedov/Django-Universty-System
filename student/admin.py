from django.contrib import admin

#Django Models 
from .models import *
from account.models import *

#Django Function
from django.db.models import Q

#Custom methods 
from abstract.admin import TypeUserAdmin

# Register your models here.

    

admin.site.register(Student,TypeUserAdmin)
admin.site.register(AdmissionStudent)
admin.site.register(RegularStudent)