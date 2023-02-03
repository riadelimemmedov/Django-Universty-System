import sys
sys.path.append('..')

from config.helpers import (get_profile_photo_upload_path, phone_message, phone_regex,
                            name_message, name_regex, random_code, slugifyNameSurname)
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from taggit.managers import TaggableManager
from django_extensions.db.fields import RandomCharField
from django_extensions.db.models import TimeStampedModel
from ckeditor.fields import RichTextField
from account.models import Account
import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models

# Create your models here.

# short path with ..


# Django Function

# Python Modules

# Helpers Function and Database Modules

# Third Party Packages


# Create your models here.


#!Designation
# => http://www.sindheducation.gov.pk/Contents/Statics/teachers-designation-wise.pdf
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
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='designation_teacher')
    father_name = models.CharField(_('father name'), max_length=50)
    is_phd = models.BooleanField(_('is phd'), default=False)
    expertise = TaggableManager(blank=True)
    # According to the semestr value
    lessons = models.ManyToManyField('school.Lesson', related_name='lessons_teacher')
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
        return '{} ({})'.format(self.account)


#!For testing
class Car(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
