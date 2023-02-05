from django.contrib import admin
from .models import *
# Register your models here.


#!TypeUserAdmin
class TypeUserAdmin(admin.ModelAdmin):    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'account':
            if 'teacher' in request.path:
                kwargs['queryset'] = Account.objects.filter(type=Account.Types.TEACHER)
            if 'student' in request.path:
                kwargs['queryset'] = Account.objects.filter(type=Account.Types.STUDENT)
        if db_field.name == 'created_by':
            if 'teacher' in request.path:
                kwargs['queryset'] = Account.objects.filter(type=Account.Types.DEAN)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)


admin.site.register(Car)