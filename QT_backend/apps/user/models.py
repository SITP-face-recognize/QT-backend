from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


def student_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(AbstractUser):
    """
    用户
    """
    USERTYPE_CHOICE = (
        ('teacher', '教师'),
        ('student', '学生')
    )
    userType = models.CharField(max_length=10, choices=USERTYPE_CHOICE, null=True, verbose_name='用户类型')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    workId = models.CharField(max_length=10, null=True, blank=True, verbose_name='教工号')
    telephone = models.CharField(max_length=15, null=True, blank=True, verbose_name="手机")
    stuId = models.CharField(max_length=10, null=True, blank=True, verbose_name='学号')
    avatar = models.ImageField(upload_to=student_avatar_path, null=True, blank=True, verbose_name='头像路径')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username
