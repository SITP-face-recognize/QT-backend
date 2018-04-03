# Generated by Django 2.0.3 on 2018-04-03 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=50, null=True, verbose_name='课程名')),
                ('courseInfo', models.TextField(blank=True, null=True, verbose_name='课程信息')),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signTime', models.DateField(auto_now_add=True, verbose_name='签到时间')),
            ],
        ),
        migrations.CreateModel(
            name='SignDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signTime', models.DateTimeField(auto_now_add=True, verbose_name='签到时间')),
                ('signKind', models.CharField(choices=[('manual', '手动'), ('face', '刷脸')], max_length=10, null=True, verbose_name='签到类型')),
                ('sign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sign_signDetail', to='course.Sign')),
            ],
        ),
    ]
