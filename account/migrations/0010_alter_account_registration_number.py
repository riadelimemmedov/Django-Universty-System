# Generated by Django 4.0 on 2023-01-26 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_account_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='registration_number',
            field=models.CharField(blank=True, db_index=True, default='CC5B88F3138', max_length=200, null=True, unique=True, verbose_name='registration number'),
        ),
    ]
