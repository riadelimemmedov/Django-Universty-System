# Generated by Django 4.0 on 2023-02-05 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_lesson_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='teacher',
        ),
    ]
