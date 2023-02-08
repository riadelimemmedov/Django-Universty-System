
#!Path
from django.urls import path

#!Views
from .views import *


#!Url
app_name = 'universty_admin'
urlpatterns = [
    path('account/',UniverstyAdminView.as_view(),name='universty_admin')
]
