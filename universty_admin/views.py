#Django Function
from django.shortcuts import render,HttpResponse
from django.db.models import Avg
from django.http import JsonResponse
from django.views.generic import *

#Helpers Function and Database Modules
from student.models import Student
from school.models import Awards
from core.models import Department

#Python Modules
from itertools import chain
from django.core import serializers
import calendar

# Create your views here.

#*getAvarageMonthRevenue
def getAvarageMonthRevenue(request):
        month_number=1
        admission_months_list = []
        while(month_number<=12):
            for i in Student.all_students.all():
                month_name = calendar.month_name[month_number]
                students = list(Student.all_students.filter(admission_date__month=month_number).aggregate(Avg('annual_paying_value')).values())
                admission_months_list.append({month_name:students})

                month_number+=1
        print('admission months list ', admission_months_list)
        return JsonResponse({'admission_months_list': admission_months_list},safe=False)




#!UniverstyAdminListView
class UniverstyAdminView(TemplateView):
    template_name = 'universty_admin/universty_admin.html'
    context_object_name='universty_admin_data'#permanent this name
    
    def get_context_data(self,**kwargs):
        studentAvaragePaying = Student.avarage_annual_payings.all()['annual_paying_value__avg']
        context = super(UniverstyAdminView, self).get_context_data(**kwargs)
        context['contextdata'] = {
                                    'students_all':Student.all_students.all(),
                                    'awards_all':Awards.awards.all(),
                                    'departments_all':Department.departments.all(),
                                    'avg_revenue':studentAvaragePaying if studentAvaragePaying != None else 0 
                                }
        return context