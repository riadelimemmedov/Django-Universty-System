# Generated by Django 4.0 on 2023-02-05 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['semester', 'registration_number'], 'verbose_name': 'Main Student'},
        ),
    ]
