#Django Function
from django.shortcuts import render,HttpResponse
from django.views.generic import *

#Helpers Function and Database Modules
from student.models import Student
from school.models import Awards
from core.models import Department

#Python Modules
from itertools import chain

# Create your views here.


def index(request):
    return HttpResponse('Hello Index Page')

#!UniverstyAdminListView
class UniverstyAdminView(TemplateView):
    template_name = 'universty_admin/universty_admin.html'
    context_object_name='universty_admin_data'#permanent this name
    
    def get_context_data(self,**kwargs):
        context = super(UniverstyAdminView, self).get_context_data(**kwargs)
        context['contextdata'] = {
                                    'students_all':Student.all_students.all(),
                                    'awards_all':Awards.awards.all(),
                                    'departments_all':Department.departments.all(),
                                    'avg_revenue':Student.avarage_annual_payings.all()['annual_paying_value__avg']
                                }
        return context
