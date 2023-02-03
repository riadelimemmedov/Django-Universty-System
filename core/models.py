
#short path with .. 
import sys

#Django Function
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator,FileExtensionValidator
from django.utils.translation import gettext_lazy as _

#Python Modules
import uuid

#Helpers Function and Database Modules
from account.models import Account
from abstract.models import Teacher
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import RandomCharField





#!SocialLink
class SocialLink(models.Model):
    user_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='account_social_media')
    media_name = models.CharField(_('media name'),max_length=50)
    url = models.URLField(_('social media url'),default='')

    def __str__(self):
        return str(self.media_name)




#!Department
class Department(TimeStampedModel):#Faculty for reqemsal iqtisadiyyat icinde amma tehlukesilizk,texnalogiya,elmler var
    name = models.CharField(_('name of department'),max_length=255,unique=True)#Infomation Technology
    short_name = models.CharField(_('department short name'),max_length=5)#IT
    code = RandomCharField(_('code'),length=12,unique=True,include_alpha=False)
    short_description = models.TextField(_('short description'),help_text='Write short description about the department.',blank=True,null=True)
    
    department_icon = models.ImageField(
        _('department icon'),
        help_text='Upload an image/icon for the department',
        upload_to='department_icon/',
        blank=True,
        null=True
    )
    head = models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True, null=True)
    current_batch = models.ForeignKey('school.Batch',on_delete=models.CASCADE,blank=True,null=True)#Hansi qruplara baxir yeni
    
    batches = models.ManyToManyField('school.Batch',_('batches'),blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True)#only create dean well know dekan

    @property
    def dept_code(self):
        if not self.code:
            return ""
        return self.code

    def __str__(self):
        return str(self.name)

    # def create_resource(self):
    #     return reverse('academics:create_department')

