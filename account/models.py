from django.db import models
from django.utils import timezone

# Create your models here.from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


from .helpers import get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex

# Create your models here.

#!MyAccountManager
class MyAccountManager(BaseUserManager):
    
    def _create_user(self,first_name,last_name,username,email,password=None,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an username')
        
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email),username=username,first_name=first_name,last_name=last_name)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,first_name,last_name,username,email,password=None,**extra_fields):        
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(first_name,last_name,username,email,password,**extra_fields)
    
    
    def create_superuser(self,first_name,last_name,email,username,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_superadmin',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        # user.is_admin=True
        # user.is_active=True
        # user.is_staff=True
        # user.is_superadmin=True
        return self._create_user(first_name,last_name,username,email,password,**extra_fields)


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
    photo = models.ImageField(upload_to=get_profile_photo_upload_path,null=True,blank=True)
    birthdate = models.DateField(_("birthdate"), null=True, blank=True)
    type = models.CharField(_('type'),max_length=20,choices=Types.choices,null=True,blank=False)
    status = models.CharField(_('status'),max_length=20,choices=Status.choices,null=True,default=Status.choices.ACTIVE)
    gender = models.CharField(_('gender'),max_length=20,choices=Gender.choices,null=True)
    payment_methods = models.ManyToManyField(_('payment_methods'),max_length=20,null=True,blank=False)
    
    date_joined = models.DateTimeField(_('date joined'),auto_now_add=True)
    last_login = models.DateTimeField(_('last login'),auto_now_add=True)
    
    password_updated_date = models.DateTimeField(_('password updated date'),default=timezone.now())
    
    
    
    
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username','phone']#this list in data macthes Account class one-by-one
    
    objects = MyAccountManager()
    
    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
    
    def clean(self) -> None:
        super().clean()
        print('self.__class__ ', self.__class__)
        self.email = self.__class__.objects.normalize_email(self.email)
    
    def get_full_name(self) -> str:
        full_name = "%s %s %s" % (self.first_name, self.last_name, self.phone)
        return full_name.strip()
    
    @property
    def full_name(self) -> str:
        return self.get_full_name()
    
    @property
    def short_name(self) -> str:
        return self.get_short_name()
    
    @property
    def name(self) -> str:
        name = "%s %s" % (self.first_name,self.last_name)
        return name.strip()
    
    def get_short_name(self) -> str:
        return self.first_name
    
    def __str__(self):
        return str(self.email)
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True
