# Generated by Django 4.0 on 2023-02-05 03:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_book_book_id_alter_library_library_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('6b76cada-145b-4411-8858-954266e03ce5'), primary_key=True, serialize=False, unique=True, verbose_name='book id'),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('3eac01bf-1988-4fae-bfc4-a8806b3d2af5'), primary_key=True, serialize=False, unique=True, verbose_name='library id'),
        ),
    ]
