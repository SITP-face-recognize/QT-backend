from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Student

# 获取自定义User
Teacher = get_user_model()


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
