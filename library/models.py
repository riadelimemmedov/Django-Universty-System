#short path with .. 
import sys
sys.path.append('..')

#Python Modules
import uuid

#Django Function
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


#Helpers Function and Database Modules
from account.models import Account
from core.models import (Department)
from school.models import (Batch)
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField


# Create your models here.


#!CategoryBook
class CategoryBook(models.Model):
    category_book_name = models.CharField(_('category book name'),max_length=50,blank=False,unique=True,db_index=True,help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    category_book_slug = models.SlugField(_('category book slug'),unique=True,db_index=True,blank=True)

    class Meta:
        verbose_name = 'Category Book'
        verbose_name_plural = 'Categoryies Book'

    def __str__(self):
        return str(self.category_book_name)
    
    def save(self,*args,**kwargs):
        self.category_book_slug = slugifyNameSurname(self.category_book_name)
        super(CategoryBook,self).save(*args,**kwargs)




#!Author
class Author(models.Model):
    author_name = models.CharField(_('name'),max_length=50,db_index=True,unique=True)
    author_surname = models.CharField(_('surname'),max_length=50)
    author_slug = models.SlugField(_('author_slug'),unique=True,db_index=True,blank=True)
    description = RichTextField(_('description'),blank=True,null=True)
    birth_date = models.DateField(_("birthdate"),null=True,blank=True)
    died_date = models.DateField(_("died_date"),null=True,blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return "{}".format(self.author_name)

    def save(self,*args,**kwargs):
        self.author_slug = slugifyNameSurname(f"{self.author_name} {self.author_surname}")
        super(Author,self).save(*args,**kwargs)


#!Book
class Book(models.Model):
    class BookChoices(models.TextChoices):
        BOOK = "book_type",_("Book Type")
        JOURNAL = "journal_type",_("Journal Type")
        CartoonHerous = "cartoon_herous_type",_("Cartoon Hereous Type")

    class LanguagesChoices(models.TextChoices):
            AFRICA = 'af',_('Afrikaans')
            ALBANIAN = 'sq',_('Albanian')
            AMHARIC = 'am',_('Amharic')
            ARABIC = 'ar',_('Arabic')
            AZERBAIJANI = 'az',_('Azerbaijani')
            BASQUE = 'eu',_('Basque')
            BELARUSIAN = 'be',_('Belarusian')
            BENGALI = 'bn',_('Bengali')
            BOSNIAN = 'bs',_('Bosnian')
            BULGARIAN = 'bg',_('Bulgarian')
            CATALAN = 'ca',_('Catalan')
            CEBUANO = 'ceb',_('Cebuano')
            CHICHEWA = 'ny',_('Chichewa')
            CORSICAN = 'co',_('Corsican')
            CROATIAN = 'hr',_('Croatian')
            CZECH = 'cs',_('Czech')
            DANISH = 'da',_('Danish')
            DUTCH = 'nl',_('Dutch')
            ENGLISH = 'eng',_('English')
            ESPERANTO = 'eo',_('Esperanto')
            ESTONIAN = 'et',_('Estonian')
            FILIPINO = 'tl',_('Filipino')
            FINNISH = 'fi',_('Finnish')
            FRENCH = 'fr',_('French')
            FRISIAN = 'fy',_('Frisian')
            GALICIAN = 'gl',_('Galician')
            GEORGIAN = 'ka',_('Georgian')
            GERMAN = 'de',_('German')
            GREEK = 'el',_('Greek')
            GUJARATI = 'gu',_('Gujarati')
            HINDI = 'hi',_('Hindi')
            HUNGARIAN = 'hu',_('Hungarian')
            INDONESIAN = 'id',_('Indonesian')
            IRISH = 'ga',_('Irish')
            ITALIAN = 'it',_('Italian')
            JAPANESE = 'ja',_('Japanese')
            CANADA = 'kn',_('Canada')
            KAZAKH = 'kk',_('Kazakh')
            KOREAN = 'ko',_('Korean')
            LATIN = 'la',_('Latin')
            LATVIAN = 'lv',_('Latvian')
            MACEDONIAN = 'mk',_('Macedonian')
            PORTUGUESE = 'pt',_('Portuguese')
            ROMANIAN = 'ro',_('Romanian')
            RUSSIAN = 'ru',_('Russian')
            SPANISH = 'es',_('Spanish')
            SWEDISH = 'sv',_('Swedish')
            TURKISH = 'tr',_('Turkish')
            UKRAINIAN = 'uk',_('Ukrainian')
            UZBEK = 'uz',_('Uzbek')
            VIETNAMESE = 'vi',_('Vietnamese')
            WELSH = 'cy',_('Welsh')

    book_id = models.CharField(_('book id'),max_length=50,db_index=True,unique=True,null=True,blank=True)    
    language = models.CharField(_('language'),max_length=50,choices=LanguagesChoices.choices)
    book_title = models.CharField(_('book title'),max_length=50)
    summary=models.TextField(_('summary'),max_length=500,null=True,blank=True,help_text="Summary about the book")
    book_author = models.ManyToManyField(Author,related_name='bookauthor')
    book_pages = models.PositiveIntegerField(default=0)    
    book_slug = models.SlugField(_('book slug'),unique=True,db_index=True,blank=True)
    book_image = models.ImageField(_('book image'),upload_to='book/',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department_book')
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryBook,on_delete=models.SET_NULL,null=True,related_name='category_book')
    book_type = models.CharField(_('book_type'),max_length=50,choices=BookChoices.choices)
    in_stock = models.BooleanField(_('in_stock'),default=False)
    available_copies = models.IntegerField(_('available_copies'),default=0)


    def __str__(self):
        return "{} ({})".format(self.book_title,self.language)
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    def save(self, *args, **kwargs):
        self.book_slug = slugifyNameSurname(self.book_title)
        self.book_id = random_code()
        super(Book,self).save(*args,**kwargs)
        


#!Library
class Library(models.Model):
    library_name = models.CharField(_('library name'),max_length=50,blank=False)
    librarian = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True,related_name='librarian_library')
    book = models.ManyToManyField(Book,related_name='book')
    library_id = models.CharField(_('library id'),max_length=50,db_index=True,unique=True,null=True,blank=True)
    
    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'libraries'
    
    def __str__(self):
        return "{} ({})".format(self.name,self.library_id)

    #*save
    def save(self,*args,**kwargs):
        #save library id
        self.library_id = random_code()
        super(Library,self).save(*args,**kwargs)

