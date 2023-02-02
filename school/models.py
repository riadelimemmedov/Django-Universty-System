
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
from account.models import Account
from teacher.models import (Teacher)
from student.models import (Student)
from core.models import (Department)
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import RandomCharField



# Create your models here.

#!Department


#!AcademicSession
class AcademicSession(TimeStampedModel):
        year = models.PositiveIntegerField(_('academic session year'),unique=True)#for example,2022 is a AcademicSession

        class Meta:
                verbose_name = 'Academic Session'
                verbose_name_plural = 'Academic Sessions'
        
        def __str__(self):
                return '{} - {}'.format(self.year, self.year + 1) #=> interval of years

        #def create_resource(self):
                #return reverse('academics:create_academic_session')

#!Batch
class Batch(TimeStampedModel):#a group of students who are taught together at school, college, or university,qrup kimi bir se
        year = models.ForeignKey(_('batch year'),AcademicSession,on_delete=models.CASCADE)
        number = models.PositiveIntegerField(_('batch number'))
        faculty_name = models.CharField(_('faculty name'),max_length=100)
        department = models.ForeignKey(_('department'),Department,on_delete=models.CASCADE)

        class Meta:
                verbose_name_plural = 'Batches'
                unique_together = ['year', 'department', 'number']

        def __str__(self):
                return f'{self.department.name} Batch {self.number} ({self.year})'



#!Subject
class Subject(models.Model):
        subject_name = models.CharField(_('subject name'),max_length=50,db_index=True,unique=True,validators=[name_regex],help_text=name_message)
        subject_number = models.PositiveIntegerField(_('subject number'),db_index=True)
        theory_marks = models.FloatField(_('theory marks'),validators=[MinValueValidator(0,0),MaxValueValidator(10.00)],blank=True,null=True)
        practical_marks = models.FloatField(_('practical marks'),validators=[MinValueValidator(0,0),MaxValueValidator(10.00)],blank=True,null=True)

        class Meta:
                ordering = ['-subject_number']
                verbose_name = 'Subject'
                verbose_name_plural = 'Subjects'
                
        def __str__(self):
                return "{} ({})".format(self.subject_name,self.subject_number)


#!Lesson
class Lesson(models.Model):
        lesson_name = models.CharField(_('lesson name'),max_length=50,validators=[name_regex],help_text=name_message)
        subject_for_lesson = models.ManyToManyField(_('subject for lesson'),Subject,related_name='subject_lesson')
        teacher = models.ForeignKey(_('teacher'),Teacher,on_delete=models.CASCADE,related_name='teacher_lesson',blank=False,null=True)
        
        #*book = models.ForeignKey(_('book),related_name='lesson_book',Book)
        #lesson_code = models.CharField(_('lesson code'),max_length=15,db_index=True,null=True,blank=True,unique=True)
        
        lesson_code = RandomCharField(_('code'),length=12,unique=True,include_alpha=False)

        def __str__(self):
                return "{} ({})".format(self.lesson_name,self.lesson_code)
        class Meta:
                verbose_name = 'Lesson'
                verbose_name_plural = 'Lessons'



#!Semestr
class Semester(TimeStampedModel):
        number = models.PositiveIntegerField(_('semester number'),unique=True)
        teacher = models.ManyToMany(('semester teacher'),Teacher,related_name='teacher_semester',null=True, blank=True)
        lessons = models.ManyToManyField(('semester lesson'),Lesson,related_name='semester_lessons')
        total_hours = models.PositiveIntegerField(_('total hours'),default=0)

        class Meta:
                ordering = ['number']

        def __str__(self):
                if self.number == 1:
                        return '1st'
                if self.number == 2:
                        return '2nd'
                if self.number == 3:
                        return '3rd'
                if self.number and 3 < self.number <= 12:
                        return '%sth' % self.number
        
        # def create_resource(self):
        #     return reverse('academics:create_semester')




#!Awards
class Awards(models.Model):
        awards_name = models.CharField(_('awards name'),max_length=100)
        owner_awards_account = models.ManyToManyField(_('owner awards account'),Account,related_name='awards_user')
        
        class Meta:
                verbose_name = 'Award'
                verbose_name_plural = 'Awards'
        
        def __str__(self):
                return str(self.awards_name)


#!Revenue
class Revenue(models.Model):
        students = models.ManyToMany(_('students'),Student,related_name='student')
        
        class Meta:
                verbose_name = 'Revenue'
                verbose_name_plural = 'Revenues'
        
        def __str__(self):
                return str(self.students__name)
