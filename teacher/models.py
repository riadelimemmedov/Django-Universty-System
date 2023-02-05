#short path with .. 
import sys
sys.path.append('..')

#Django Function
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator,FileExtensionValidator
from django.utils.translation import gettext_lazy as _

#Python Modules
import uuid

#Helpers Function and Database Modules
from account.models import Account
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import RandomCharField



#!Designation
# => http://www.sindheducation.gov.pk/Contents/Statics/teachers-designation-wise.pdf 
# Elementary school teachers.
# Middle school teachers.
# High school teachers.
# Special education teachers.
# ESL teachers.

class Designation(TimeStampedModel):
    title = models.CharField(_('title'), max_length=255)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'

    def __str__(self):
        return str(self.title)


#!Teacher
class Teacher(TimeStampedModel):
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='account_teacher')    
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE, related_name='designation_teacher')
    father_name = models.CharField(_('father name'), max_length=50)
    is_phd = models.BooleanField(_('is phd'), default=False)
    expertise = models.CharField(_('expertise'),max_length=50,default='')
    # According to the semestr value
    semestr = models.ManyToManyField('school.Semester',related_name='teacher_semester',blank=True)
    
    joining_date = models.DateField(auto_now=True)

    created_by = models.ForeignKey(  # only director give position
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING, null=True
    )

    class Meta:
        ordering = ['joining_date']
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return '{}' .format(self.account)