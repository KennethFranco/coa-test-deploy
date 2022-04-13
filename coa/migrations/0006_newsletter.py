# Generated by Django 3.2.6 on 2022-03-10 13:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coa', '0005_office_office_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('date', models.DateField(default=None)),
                ('photo', models.FileField(default='null', upload_to='')),
                ('photoCaption', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]