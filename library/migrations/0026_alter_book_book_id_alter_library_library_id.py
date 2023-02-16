# Generated by Django 4.0 on 2023-02-08 15:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0025_alter_book_book_id_alter_library_library_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('2a3409eb-fe43-48d7-b26c-b10fe2cce573'), primary_key=True, serialize=False, unique=True, verbose_name='book id'),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('890a026e-7219-43dd-9bac-3617ea187415'), primary_key=True, serialize=False, unique=True, verbose_name='library id'),
        ),
    ]