
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
from config.helpers import (get_profile_photo_upload_path,phone_message,phone_regex,name_message,name_regex,random_code,slugifyNameSurname)

#Third Party Packages
from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel


# Create your models here.


class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_alumni=False,is_dropped=False)

class AlumniManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_alumni=True)

class RegularStudent(TimeStampedModel):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)

    entered_date = models.DateField(auto_now=True)
    finished_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student.name} {self.semester}"


class Student(TimeStampedModel):
    class BoyGirlSelect(models.TextChoices):
        BOY = "boy",_("Boy")
        GIRL = "girl",_("Girl")


    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)    
    admission_student = models.ForeignKey(AdmissionStudent,on_delete=models.CASCADE)
    roll = models.CharField(max_length=6, unique=True, blank=True, null=True)
    registration_number = models.CharField(max_length=6,unique=True,)#\
    registration_number = models.UUIDField(max_length=6,db_index=True,unique=True,default=uuid.uuid4)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    ac_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE,blank=True, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,blank=True, null=True, related_name='students')
    guardian_mobile = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")

    group_number = models.CharField(max_length=100)
    number_of_lessons = models.IntegerField(default=6)

    is_alumni = models.BooleanField(default=False)
    is_dropped = models.BooleanField(default=False)

    # Managers
    objects = StudentManager()
    alumnus = AlumniManager()

    class Meta:
        ordering = ['semester', 'roll', 'registration_number']

    def __str__(self):
        return '{} ({}) semester {} dept.'.format(
            self.admission_student.name,
            self.semester,
            self.admission_student.choosen_department
        )

    def _find_last_admitted_student_serial(self):
        # What is the last temp_id for this year, dept?
        item_serial_obj = TempSerialID.objects.filter(
            department=self.admission_student.choosen_department,
            year=self.ac_session,
        ).order_by('serial').last()

        if item_serial_obj:
            # Return last temp_id
            serial_number = item_serial_obj.serial
            return int(serial_number)
        else:
            # If no temp_id object for this year and department found
            # return 0
            return 0
    
    def get_temp_id(self):
        # Get current year (academic) last two digit
        year_digits = str(self.ac_session.year)[-2:]
        # Get batch of student's department
        batch_digits = self.batch.number
        # Get department code
        department_code = self.admission_student.choosen_department.code
        # Get admission serial of student by department
        temp_serial_key = self.temp_serial
        # return something like: 21-15-666-15
        temp_id = f'{year_digits}-{batch_digits}-' \
                    f'{department_code}-{temp_serial_key}'
        return temp_id

    def save(self, *args, **kwargs):
        # Check if chosen_dept == batch.dept is same or not.
        if self.admission_student.choosen_department != self.batch.department:
            raise OperationalError(
                f'Cannot assign {self.admission_student.choosen_department} '
                f'departments student to {self.batch.department} department.')
        elif self.admission_student.choosen_department == self.batch.department:
            # Set AdmissionStudent assigned_as_student=True
            self.admission_student.assigned_as_student = True
            self.admission_student.save()

        # Create temporary id for student id if temporary_id is not set yet.
        if not self.temp_serial or not self.temporary_id:
            last_temp_id = self._find_last_admitted_student_serial()
            current_temp_id = str(last_temp_id + 1)
            self.temp_serial = current_temp_id
            self.temporary_id = self.get_temp_id()
            super().save(*args, **kwargs)
            try:
                with transaction.atomic():  
                    temp_serial_id = TempSerialID.objects.create(
                        student=self,
                        department=self.admission_student.choosen_department,
                        year=self.ac_session,
                        serial=current_temp_id
                    )
                    temp_serial_id.save()
            except IntegrityError:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ Override delete method """
        # If student is deleted, AdmissionStudent.assigned_as_student
        # should be false.
        self.admission_student.assigned_as_student = False
        self.admission_student.save(*args, **kwargs)


class AdmissionStudent(Student):
    APPLICATION_TYPE_CHOICE = (
        ('1', 'Online'),
        ('2', 'Offline')
    )
    EXAM_NAMES = (
        ('HSC', 'Higher Secondary Certificate'),
        ('SSC', 'Secondary School Certificate'),
        ('DAKHIL', 'Dakhil Exam'),
        ('VOCATIONAL', 'Vocational'),
    )
    counseling_by = models.ForeignKey(Teacher, related_name='counselors',on_delete=models.CASCADE, null=True)
    counsel_comment = models.ManyToManyField(CounselingComment,blank=True)
    choosen_department = models.ForeignKey(
        Department, related_name='admission_students',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    exam_name = models.CharField(
        'Exam Name',
        choices=EXAM_NAMES,
        max_length=10
    )
    passing_year = models.CharField(max_length=4)
    group = models.CharField(max_length=15)
    board = models.CharField(max_length=100)
    gpa = models.DecimalField(
        decimal_places=2,
        max_digits=4
    )
    marksheet_image = models.ImageField(#cv kimi bir sey
        "Upload Your Marksheet",
        upload_to='students/applicants/marksheets/',
        blank=True, null=True
    )
    admission_policy_agreement = models.BooleanField(
        """
        এই মর্মে অঙ্গীকার করছি যে, ভর্তি হওয়ার সুযোগ পেলে আমি অত্র শিক্ষা প্রতিষ্ঠান ও 
        বাংলাদেশ কারিগরি শিক্ষা বোর্ডের যাবতীয় আইনকানুন মেনে চলব এবং কোন অবস্থাতেই অত্র শিক্ষা প্রতিষ্ঠান, বাংলাদেশ কারিগরি শিক্ষা বোর্ড 
        এবং দেশের আইনের পরিপন্থি কোন কাজে লিপ্ত হব না
        """,
        default=False
    )
    admitted = models.BooleanField(default=False)
    admission_date = models.DateField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    application_type = models.CharField(
        max_length=1,
        choices=APPLICATION_TYPE_CHOICE,
        default='1'
    )
    migration_status = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    rejected = models.BooleanField(default=False)
    assigned_as_student = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.department_choice != self.choosen_department:
            status = f'From {self.department_choice} to {self.choosen_department}'
            self.migration_status = status
            super().save(*args, **kwargs)
        super().save(*args, **kwargs)

