from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from .models import *

import os
# Register your models here.


#!AccoutAdmin
@admin.register(Account)
class AccountAdmin(UserAdmin):
    
    #thumbnail
    def thumbnail(self,object):
        if(object.photo):
            return format_html('<img src="{}" width="35" style="border-radius:50%;">'.format(object.photo.url))
        else:
            return format_html('<img src="https://i.stack.imgur.com/l60Hf.png" width="35" style="border-radius:50%;">')
        
    fieldsets = (
        (None,{"fields":('email','phone','password')}),
        (
            _('Personal info'),
            {
                "fields":(
                    "first_name",
                    "last_name",
                    'type',
                    "photo",
                    "background_picture",
                    "headline",
                    "show_headline_in_bio",
                    "summary",
                    "country",
                    "city",
                    "date_of_admission",
                    "registration_number"
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields":("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "type",
                    "password1",
                    "password2",
                    "photo",
                    "background_picture",
                    "headline",
                    "show_headline_in_bio",
                    "summary",
                    "country",
                    "city",
                ),
            },
        ),
    )
    list_display = ("first_name","last_name","phone","is_staff","date_joined","last_login","thumbnail")
    list_filter = ("is_staff","is_superuser","is_admin","is_superadmin","is_active")
    list_display_links = ("thumbnail","first_name","last_name")
    search_fields = ("first_name", "last_name","email", "phone")
    readonly_fields = ("date_joined","last_login")


