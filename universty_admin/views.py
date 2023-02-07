#Django Methods
from django.shortcuts import render,HttpResponse
from django.views.generic import *

# Create your views here.


#!UniverstyAdminListView
class UniverstyAdminListView(TemplateView):
    template_name = 'universty_admin/universty_admin.html'
    context_object_name='universtyadmin'#permanent this name
    
    def get_context_data(self,**kwargs):
        context = super(UniverstyAdminListView, self).get_context_data(**kwargs)
        context['data'] = 'Hello UniverstyAdmin From Backend'
        return context