from django.contrib import admin
from .models import *

# Register your models here.


#!SocialLinkAdmin
# @admin.register(SocialLink)
# class SocialLinkAdmin(admin.ModelAdmin):
#     list_display = ['user_account','media_name','url']

admin.site.register(SocialLink)
admin.site.register(Department)

