# Generated by Django 2.2.6 on 2020-05-21 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20200521_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='join_date',
        ),
    ]
