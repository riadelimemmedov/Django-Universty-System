from django.db import models
from account.models import *

# Create your models here.


#!SocialLink
# class SocialLink(models.Model):
#     user_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='account_social_media')
#     media_name = models.CharField(max_length=50)
#     url = models.URLField(default='')

#     def __str__(self):
#         return str(self.media_name)