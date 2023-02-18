# Generated by Django 3.2 on 2023-02-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_admissionstudent_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissionstudent',
            name='admission_date',
        ),
        migrations.RemoveField(
            model_name='admissionstudent',
            name='passing_year',
        ),
        migrations.AddField(
            model_name='student',
            name='admission_date',
            field=models.DateField(blank=True, null=True, verbose_name='admission date'),
        ),
        migrations.AddField(
            model_name='student',
            name='passing_year',
            field=models.CharField(default=1, max_length=4, verbose_name='passing year'),
            preserve_default=False,
        ),
    ]
