from django.contrib import admin

#Django models
from .models import *

from abstract.admin import TypeUserAdmin

# Register your models here.
admin.site.register(AcademicSession)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Semester)
admin.site.register(Awards,TypeUserAdmin)
admin.site.register(Revenue)