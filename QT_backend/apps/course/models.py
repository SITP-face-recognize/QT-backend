from django.db import models
from user.models import Teacher, Student


# Create your models here.


class Course(models.Model):
    """
    课程
    """
    courseName = models.CharField(max_length=50, null=True, verbose_name="课程名")
    teacher = models.ManyToManyField(Teacher, verbose_name='教师')
    student = models.ManyToManyField(Student, verbose_name='学生')


class Sign(models.Model):
    """
    签到表
    """
    SIGNKIND_CHOICE = (
        ('manual', '手动'),
        ('face', '刷脸')
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    signTime = models.DateField(auto_now_add=True, verbose_name="签到时间")
    signKind = models.CharField(max_length=10, verbose_name='签到类型')
