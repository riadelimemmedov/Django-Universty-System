from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(AcademicSession)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Semester)
admin.site.register(Awards)
admin.site.register(Revenue)