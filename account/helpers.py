import os
from datetime import datetime
from random import randint
from time import time

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from PIL import Image

phone_message = _('Phone number must be in this format:994xxxxxxxxx')
name_message = _("Name contains only a-z and A-Z characters")
phone_regex = RegexValidator(regex=r"994\s?\d{2}[2-9]\d{6}",message=phone_message)
name_regex = RegexValidator(regex=r"[a-zA-Z\s']+",message=name_message)

symbols_mapping = [
    (" ", "-"),
    (".", "."),
    (",", "-"),
    ("!", "-"),
    ("?", "-"),
    ("'", "-"),
    ('"', "-"),
]

lower_case_mapping = [
    ("ə", "e"),
    ("ı", "i"),
    ("ö", "o"),
    ("ğ", "g"),
    ("ü", "u"),
    ("ş", "s"),
    ("ç", "c"),
]

upper_case_mapping = [
    ("Ə", "E"),
    ("İ", "I"),
    ("Ö", "O"),
    ("Ğ", "G"),
    ("Ü", "U"),
    ("Ş", "S"),
    ("Ç", "C"),
]


#!generate_file_path
def generate_file_path(base:str,filename):
    today = datetime.today()
    name,extension = os.path.splitext(filename)
    return f"{base}/{today.year}/{today.month}/{slugify(name)}-{str(randint(100000, 999999))}{extension}"


#!get_profile_photo_upload_path
def get_profile_photo_upload_path(instance,filename):
    return generate_file_path('profile',filename)


#!slugify
def slugify(text:str) -> str:#*return string value
    mapping:list = symbols_mapping+lower_case_mapping
    text = text.lower()
    print('text value in slugify image ', text)
    
    for before,after in mapping:
        print('before value in slugify methods ', before)
        print('after value in slugify methods ', before)
        text = text.replace(before,after)
    return text
    