from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

def student_avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)



class Teacher(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    telephone = models.CharField(max_length=15, null=True, verbose_name="手机")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.username


class Student(models.Model):
    """
    学生
    """
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(max_length=30, null=True, verbose_name="姓名")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='Male', verbose_name='性别')
    stuId = models.CharField(max_length=10, null=True, verbose_name='学号')
    avatar = models.ImageField(upload_to=student_avatar_path)
