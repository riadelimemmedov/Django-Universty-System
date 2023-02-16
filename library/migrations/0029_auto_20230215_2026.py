# Generated by Django 3.2 on 2023-02-15 16:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0028_alter_book_book_id_alter_library_library_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('9a96f9a8-9b5d-4139-8e12-d3581b71e859'), primary_key=True, serialize=False, unique=True, verbose_name='book id'),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('f26fd481-4fb3-4aed-853c-ba7aa200a32c'), primary_key=True, serialize=False, unique=True, verbose_name='library id'),
        ),
    ]