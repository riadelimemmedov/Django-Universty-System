# Generated by Django 4.0 on 2023-01-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_account_registration_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='registration_number',
            field=models.CharField(db_index=True, default='3D585A951B4', max_length=200, null=True, unique=True, verbose_name='registration number'),
        ),
    ]
