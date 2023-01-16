from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from PIL import Image

phone_message = _('Phone number must be in this format:994xxxxxxxxx')
name_message = _("Name contains only a-z and A-Z characters")
phone_regex = RegexValidator(regex=r"994\s?\d{2}[2-9]\d{6}",message=phone_message)
name_regex = RegexValidator(regex=r"[a-zA-Z\s']+",message=name_message)