
#short path with .. 
import sys
sys.path.append('..')

#Django Function
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,FileExtensionValidator
from django.utils.translation import gettext_lazy as _

#Python Modules
import uuid

#Helpers Function and Database Modules
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel



# Create your models here.



#!AcademicSession
# class AcademicSession(TimeStampedModel):
#     year = models.PositiveIntegerField(_('academic session year'),unique=True)#for example,2022 is a AcademicSession

#     def __str__(self):
#         return '{} - {}'.format(self.year, self.year + 1) #=> interval of years
    
#     def create_resource(self):
#         return reverse('academics:create_academic_session')

#!Batch
# class Batch(TimeStampedModel):#a group of students who are taught together at school, college, or university,qrup kimi bir se
#     year = models.ForeignKey(_('batch year'),AcademicSession,on_delete=models.CASCADE)
#     number = models.PositiveIntegerField(_('batch number'))
#     faculty_name = models.CharField(_('faculty name'),max_length=100)
#     department = models.ForeignKey(_('department'),Department,on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = 'Batches'
#         unique_together = ['year', 'department', 'number']

#     def __str__(self):
#         return f'{self.department.name} Batch {self.number} ({self.year})'



#!Lesson
# class Lesson(models.Model):
#     lesson_name = models.CharField(_('lesson name'),max_length=50,validators=[name_regex],help_text=name_message)
#     # subject_for_lesson = models.ManyToManyField(_('subject for lesson'),Subject,related_name='subject_lesson')
#     # instructor = models.ForeignKey(_('instructor'),Teacher,on_delete=models.CASCADE,related_name='instrucor_lesson',blank=False,null=True)
#       book = models.ForeignKey(_('book),related_name='lesson_book',Book)
#     lesson_code = models.CharField(_('lesson code'),max_length=15,db_index=True,null=True,blank=True,unique=True)

    
#     # def __str__(self):
        #   return "{} ({})".format(self.lesson_name,self.lesson_code)
#      
    
#     class Meta:
#         verbose_name = 'Lesson'
#         verbose_name_plural = 'Lessons'


#!Subject
# class Subject(models.Model):
#     subject_name = models.CharField(_('subject name'),max_length=50,db_index=True,unique=True,validators=[name_regex],help_text=name_message)
#     subject_number = models.PositiveIntegerField(_('subject number'),db_index=True)
#     theory_marks = models.FloatField(_('theory marks'),validators=[MinValueValidator(0,0),MaxValueValidator(10.00)],blank=True,null=True)
#     practical_marks = models.FloatField(_('practical marks'),validators=[MinValueValidator(0,0),MaxValueValidator(10.00)],blank=True,null=True)
    

#     class Meta:
#         ordering = ['-subject_number']
#         verbose_name = 'Subject'
#         verbose_name_plural = 'Subjects'
        
#     def __str__(self):
#         return "{} ({})".format(self.subject_name,self.subject_number)


#!Department
# class Department(TimeStampedModel):#Fakulte
#     name = models.CharField(_('name of department'),max_length=255,unique=True)#Infomation Technology
#     short_name = models.CharField(_('department short name'),max_length=5)#IT
#     code = RandomCharField(_('code number'),length=12,unique=True,include_alpha=False)
#     short_description = models.TextField(_('short description'),help_text='Write short description about the department.',blank=True,null=True)
    
#     department_icon = models.ImageField(
#         _('department icon'),
#         help_text='Upload an image/icon for the department',
#         upload_to='department_icon/',
#         blank=True,
#         null=True
#     )
#     # * not exists yet <Teacher> module => head = models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True, null=True)
    
#     #* not exits yet <Batch> current_batch = models.ForeignKey('Batch', on_delete=models.CASCADE,blank=True, null=True,#Hansi qruplara baxir yeni
#     #     related_name='current_batches'#Indi hansi qrupdu secilen ile gore
#     # )
#     # batches = models.ManyToManyField(#Umimi neler ola biler
#     #     'Batch',
#     #     related_name='department_batches',
#     #     blank=True
#     # )
#     created_by = models.ForeignKey(
#         _('created by'),
#         settings.AUTH_USER_MODEL,
#         on_delete=models.DO_NOTHING,
#         null=True
#     )

#     @property
#     def dept_code(self):
#         if not self.code:
#             return ""
#         return self.code

#     def __str__(self):
#         return str(self.name)

#     def create_resource(self):
#         return reverse('academics:create_department')



