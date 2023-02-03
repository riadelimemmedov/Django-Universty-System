
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
from school.models import (AcademicSession,Semester,Batch)
from core.models import (Department)
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField
from django_extensions.db.models import TimeStampedModel


# Create your models here.


#*StudentManager
class StudentManager(models.Manager):
      def get_queryset(self):
            return super().get_queryset().filter(is_alumni=False,is_dropped=False)


#*AlumniManager
class AlumniManager(models.Manager):
      def get_queryset(self):
            return super().get_queryset().filter(is_alumni=True)


#!StudentBase
class StudentBase(TimeStampedModel):
      TRIBAL_STATUS = (
            (1, 'Yes'),
            (0, 'No'),
      )
      CHILDREN_OF_FREEDOM_FIGHTER = (
            (1, 'Yes'),
            (0, 'No'),
      )
      fathers_name = models.CharField(_("Father's Name"),max_length=100)
      mothers_name = models.CharField(_("Mother's Name"),max_length=100)
      current_address = models.TextField(_('current adress'))
      permanent_address = models.TextField(_('permanent adress'))
      guardian_mobile_number = models.CharField(_('guardian mobile number'),validators=[phone_regex],max_length=12,blank=True,null=True,unique=True,help_text=phone_message)
      is_orphan = models.BooleanField(_('orphan'),default=False)
      
      tribal_status = models.PositiveSmallIntegerField(
            choices=TRIBAL_STATUS,default=0
      )
      children_of_war_fighter = models.PositiveSmallIntegerField(
            choices=TRIBAL_STATUS,default=0
      )
      department_choice = models.ForeignKey(
            Department,
            on_delete=models.CASCADE
      )
      class Meta:
            abstract = True
      
      def __str__(self):
            return str(self.name)

#!Student
class Student(TimeStampedModel):
      class BoyGirlSelect(models.TextChoices):
            BOY = "boy",_("Boy")
            GIRL = "girl",_("Girl")


      account = models.ForeignKey(Account,on_delete=models.CASCADE)    
    # admission_student = models.ForeignKey(AdmissionStudent,on_delete=models.CASCADE)
      gender = models.CharField(_('gender'),max_length=6,unique=True,blank=True,null=True,choices=BoyGirlSelect.choices)
    # registration_number = models.CharField(max_length=6,unique=True,)#\
      registration_number = models.UUIDField(_('registration number'),max_length=6,db_index=True,unique=True,default=uuid.uuid4)
      semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
      ac_session = models.ForeignKey(AcademicSession,on_delete=models.CASCADE,blank=True, null=True)
      batch = models.ForeignKey(Batch,on_delete=models.CASCADE,blank=True, null=True, related_name='students')
      guardian_mobile = models.CharField(_('guardian mobile'),validators=[phone_regex],max_length=12,blank=True,null=True,unique=True,help_text=phone_message)
      annual_paying_value= MoneyField(max_digits=14, decimal_places=2, default_currency='USD') #This is money field

      group_number = models.CharField(_('group number'),max_length=10)
      number_of_lessons = models.IntegerField(_('number of lessons'),default=48)

      is_alumni = models.BooleanField(default=False)
      is_dropped = models.BooleanField(default=False)

      # Managers
      objects = StudentManager()
      alumnus = AlumniManager()

      class Meta:
            ordering = ['semester','registration_number']

      def __str__(self):
            return '{} ({}) semester {} dept.'.format(
                  self.admission_student.name,
                  self.semester,
                  self.admission_student.choosen_department
            )

#!AdmissionStudent
class AdmissionStudent(Student):
      APPLICATION_TYPE_CHOICE = (
            ('1', 'Online'),
            ('2', 'Offline')
      )
      EXAM_NAMES = (
            ('DIM', 'State  Of Exam Center'),
            ('College', 'College Exam'),
            ('VOCATIONAL', 'Vocational'),
      )

      choosen_department = models.ForeignKey(
            Department,
            related_name='admission_students',
            on_delete=models.CASCADE,
            blank=True, null=True
      ),
      exam_name = models.CharField(
            _('exam name'),
            'Exam Name',
            choices=EXAM_NAMES,
            max_length=10
      )
      passing_year = models.CharField(_('passing year'),max_length=4)
      group = models.CharField(_('group'),max_length=15)
      board = models.CharField(_('board'),max_length=100)
      gpa = models.DecimalField(decimal_places=2,max_digits=4)#ortalama giris bali filan
      marksheet_image = models.ImageField(_('marksheet image'),upload_to='students/applicants/marksheets/',blank=True, null=True)#cv kimi bir sey
      admission_policy_agreement = models.BooleanField(
            _('admission policy aggrement'),
            """
                  If I get the opportunity to be accepted, I promise to abide by all laws and regulations of this educational institution and Azerbaijan Technical Education Board and not take any action against the educational institution, Bangladesh Technical Education Board and laws. country anyway
            """,
            default=False
      ),
      admitted = models.BooleanField(_('is admitted'),default=False)
      admission_date = models.DateField(_('admission date'),blank=True,null=True)
      paid = models.BooleanField(default=False)
      application_type = models.CharField(
            _('apllication type'),
            max_length=1,
            choices=APPLICATION_TYPE_CHOICE,
            default='2'
      )
      migration_status = models.CharField(
            _('migration status'),
            max_length=255,
            blank=True,null=True
      )
      rejected = models.BooleanField(default=False)
      assigned_as_student = models.BooleanField(default=False)

      class Meta:
            verbose_name = 'Student'
            verbose_name_plural = 'Students'

      def __str__(self):  
            return f"{self.name}"


#!RegularStudent
class RegularStudent(TimeStampedModel):
      student = models.ForeignKey(Student,on_delete=models.CASCADE)
      semester = models.ForeignKey(Semester,on_delete=models.CASCADE)

      def __str__(self):
            return f"{self.student.name} {self.semester}"
