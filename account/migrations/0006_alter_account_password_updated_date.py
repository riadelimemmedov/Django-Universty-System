# Generated by Django 4.0 on 2023-01-18 19:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_account_password_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 18, 19, 17, 0, 631980, tzinfo=utc), verbose_name='password updated date'),
        ),
    ]