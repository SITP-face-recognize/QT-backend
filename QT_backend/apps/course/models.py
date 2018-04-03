from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# 获取自定义User
User = get_user_model()


class Course(models.Model):
    """
    课程
    """
    courseName = models.CharField(max_length=50, null=True, verbose_name='课程名')
    courseInfo = models.TextField(null=True, blank=True, verbose_name='课程信息')
    teacher = models.ManyToManyField(User, verbose_name='教师', related_name='teacher_course')
    student = models.ManyToManyField(User, verbose_name='学生', related_name='student_course')




class Sign(models.Model):
    """
    签到表
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_sign')
    student = models.ManyToManyField(User, through='SignDetail', related_name='student_sign')
    signTime = models.DateField(auto_now_add=True, verbose_name="签到时间")


class SignDetail(models.Model):
    """
    签到详情
    """
    SIGNKIND_CHOICE = (
        ('manual', '手动'),
        ('face', '刷脸')
    )
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE, related_name='sign_signDetail')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sign_signDetail')
    signTime = models.DateTimeField(auto_now_add=True, verbose_name='签到时间')
    signKind = models.CharField(max_length=10, choices=SIGNKIND_CHOICE, null=True, verbose_name='签到类型')

    class Meta:
        unique_together = ("sign", "student",)
