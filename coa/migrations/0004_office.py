# Generated by Django 3.2.6 on 2022-03-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coa', '0003_auto_20220310_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('officer_name', models.CharField(max_length=100)),
                ('officer_position', models.CharField(max_length=100)),
                ('officer_photo', models.FileField(default='null', upload_to='')),
                ('officer_email', models.EmailField(max_length=254)),
            ],
        ),
    ]