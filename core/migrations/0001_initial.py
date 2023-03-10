# Generated by Django 4.0 on 2023-02-04 04:25

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name of department')),
                ('short_name', models.CharField(max_length=5, verbose_name='department short name')),
                ('code', django_extensions.db.fields.RandomCharField(blank=True, editable=False, include_alpha=False, length=12, unique=True, verbose_name='code')),
                ('short_description', models.TextField(blank=True, help_text='Write short description about the department.', null=True, verbose_name='short description')),
                ('department_icon', models.ImageField(blank=True, help_text='Upload an image/icon for the department', null=True, upload_to='department_icon/', verbose_name='department icon')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_name', models.CharField(max_length=50, verbose_name='media name')),
                ('url', models.URLField(default='', verbose_name='social media url')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_social_media', to='account.account')),
            ],
        ),
    ]
