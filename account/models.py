# Create your models here.from django.db import models

#short path with .. 
import sys
sys.path.append('..')


#Python Modules
import os
import uuid

#Django Function
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

#Helpers Function and Database Modules
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code)


#Third Party Packages
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

# Create your models here.

#!MyAccountManager
class MyAccountManager(BaseUserManager):
    
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,email,password=None,**extra_fields):        
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_superadmin',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email,password,**extra_fields)


#!Account
class Account(AbstractBaseUser,PermissionsMixin):

    class Types(models.TextChoices):#?+
        ADMIN = "ADMIN",_('admin'),
        STUDENT = "STUDENT",_('student')
        TEACHER = "TEACHER",_('teacher')
        DRIVER = "DRIVER",_('driver')
        HOSTEL = "HOSTEL",_('hostel')
        COACH = "COACH",_('coache')
        LIBRARIAN = "LIBRARIAN",_('librarian')
        
    class Status(models.TextChoices):#?+
        ACTIVE = "ACTIVE",_('active')
        INACTIVE = "INACTIVE",_('inactive')
        
    class Gender(models.TextChoices):#?+
        MALE = "MALE",_("male")
        FEMALE = "FEMALE",_("female")
        
    class PaymentMethods(models.TextChoices):#?+
        PAYPAL = "PAYPAL",_('paypal')
        STRIP = "STRIP",_('strip')
        PAYSTACK = "PAYSTACK",_('paystack')
    
    #!Mail Column
    email = models.EmailField(_('email'),max_length=100,unique=True)
    first_name = models.CharField(_('first name'),max_length=150,blank=True,validators=[name_regex],help_text=name_message)
    last_name = models.CharField(_('last name'),max_length=150,blank=True,validators=[name_regex],help_text=name_message)
    username = models.CharField(_('username'),max_length=150,blank=True,validators=[name_regex],help_text=name_message)
    is_admin = models.BooleanField(_('admin status'),default=False,help_text=_('Designates whether the user is admin or not.'))
    is_staff = models.BooleanField(_('staff status'),default=False,help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'),default=True,help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_superadmin = models.BooleanField(_('superadmin'),default=False,help_text=_('Designates whether the user is admin or not.'))
    phone = models.CharField(_('phone'),validators=[phone_regex],max_length=12,blank=True,null=True,unique=True,help_text=phone_message)
    
    
    
    #!Extra Profile Data
    photo = models.ImageField(upload_to=get_profile_photo_upload_path,null=True,blank=False)
    
    ###
    background_picture = models.ImageField(upload_to='background-picture/',null=True,blank=True)
    headline = models.CharField(_('headline'),max_length=255,null=True,blank=True)
    show_headline_in_bio = models.BooleanField(_('I want to use this as my bio'),default=False)
    summary = RichTextUploadingField(_('Your Profile Summary'),blank=True,null=True)
    country = models.ForeignKey('cities_light.Country',on_delete=models.SET_NULL,null=True) 
    city = models.ForeignKey('cities_light.City',on_delete=models.SET_NULL, null=True)
    adress = models.CharField(_('adress'),max_length=50,null=True)
    date_of_admission = models.DateField(_('date of admission'),null=True)
    registration_number = models.CharField(_('registration number'),max_length=50,db_index=True,null=True,blank=True,unique=True)
    # father_name = models.CharField(_("father's name"), max_length=150,null=True,validators=[name_regex], help_text=name_message)
    website_links = models.URLField(_('website links'),default='')
    ###


    birthdate = models.DateField(_("birthdate"),null=True,blank=True)
    type = models.CharField(_('type'),max_length=20,choices=Types.choices,null=True,blank=False)
    status = models.CharField(_('status'),max_length=20,choices=Status.choices,null=True,default=Status.choices[0][0])
    gender = models.CharField(_('gender'),max_length=20,choices=Gender.choices,null=True)
    payment_methods = MultiSelectField(_('payment_methods'),max_length=20,null=True,blank=False)
    
    date_joined = models.DateTimeField(_('date joined'),auto_now_add=True)
    last_login = models.DateTimeField(_('last login'),auto_now_add=True)
    
    password_updated_date = models.DateTimeField(_('password updated date'),auto_now_add=True)
    
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username','phone']#this list in data macthes Account class one-by-one
    
    objects = MyAccountManager()
    
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        ordering = ['first_name','last_name','username']
    
    
    #*save
    def save(self,*args,**kwargs):
        #save registration_number
        self.registration_number = random_code()
        super(Account,self).save(*args,**kwargs)
    
    #*clean
    def clean(self) -> None:
        super().clean()
        print('self.__class__ ', self.__class__)
        self.email = self.__class__.objects.normalize_email(self.email)
    
    #*get_full_name
    def get_full_name(self) -> str:
        full_name = "{} {} {}".format(self.first_name,self.last_name,self.phone)
        return full_name.strip()
    
    #*full_name
    @property
    def full_name(self) -> str:
        return self.get_full_name()
    
    
    #*short_name
    @property
    def short_name(self) -> str:
        return self.get_short_name()
    
    
    #*name
    @property
    def name(self) -> str:
        name = "{} {}".format(self.first_name,self.last_name)
        return name.strip()
    
    
    #*get_short_name
    def get_short_name(self) -> str:
        return self.first_name
    
    
    #*mobile_phone
    def mobile_phone(self) -> str or None:
        if self.phone:
            return "+" + self.phone
        return None
    
    #*set_password
    def set_password(self,raw_password):
        super().set_password(raw_password)
        self.password_updated_date = timezone.now()
    
    
    """#?email_user not using yet
        #  def email_user(self, subject, message, from_email=None, delay=True) -> bool:
        #         end an email to this user
        #     if not from_email:
        #         from_email = settings.EMAIL_HOST_USER
        #     if not self.email:
        #         return False
        #     if settings.ENVIRONMENT == "LOCAL":
        #         send_email(subject, message, from_email, self.email)
        #     elif not delay:
        #         send_email(subject, message, from_email, self.email)
        #     else:
        #         send_email.delay(subject, message, from_email, self.email)
        #return True 
    # """

    
    #*__str__
    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name} {self.registration_number}"
    
    #*__has_perm__
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    
    #*has_module_perms    
    def has_module_perms(self,add_label):
        return True



