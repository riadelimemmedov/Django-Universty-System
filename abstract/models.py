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

from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import RandomCharField

#!For testing
class Car(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
