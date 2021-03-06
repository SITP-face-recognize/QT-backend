# Generated by Django 2.0.3 on 2018-04-03 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signdetail',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sign_signDetail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sign',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_sign', to='course.Course'),
        ),
        migrations.AddField(
            model_name='sign',
            name='student',
            field=models.ManyToManyField(related_name='student_sign', through='course.SignDetail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(related_name='student_course', to=settings.AUTH_USER_MODEL, verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher_course', to=settings.AUTH_USER_MODEL, verbose_name='教师'),
        ),
        migrations.AlterUniqueTogether(
            name='signdetail',
            unique_together={('sign', 'student')},
        ),
    ]
