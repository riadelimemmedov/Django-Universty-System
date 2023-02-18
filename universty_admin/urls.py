
#!Path
from django.urls import path

#!Views
from .views import *


#!Url
app_name = 'universty_admin'
urlpatterns = [
    #Class Based View
    path('account/',UniverstyAdminView.as_view(),name='universty_admin'),
    
    #Function Based View
    path('get/avg/month/revenue',getAvarageMonthRevenue,name='get_avg_month_revenue'),
    
]
