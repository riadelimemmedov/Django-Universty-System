# Generated by Django 4.0 on 2023-02-05 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='expertise',
        ),
        migrations.AddField(
            model_name='teacher',
            name='expertise',
            field=models.CharField(default=1, max_length=50, verbose_name='expertise'),
            preserve_default=False,
        ),
    ]
