# Generated by Django 2.2.6 on 2020-05-26 12:51

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_photo_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='desc',
            field=models.CharField(max_length=255, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True, verbose_name=''),
        ),
    ]
