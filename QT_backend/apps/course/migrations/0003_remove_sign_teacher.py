# Generated by Django 2.0.2 on 2018-03-24 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20180324_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sign',
            name='teacher',
        ),
    ]
