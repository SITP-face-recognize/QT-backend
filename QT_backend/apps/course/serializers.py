from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Course,Sign

# 获取自定义User
Teacher = get_user_model()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = '__all__'

class TeacherCourseListSerializer(serializers.ModelSerializer):
    courseId=serializers.ReadOnlyField(source='course_set.id')
    courseName=serializers.ReadOnlyField(source='course_set.courseName')
    class Meta:
        model = Teacher
        fields=('courseId','courseName')


class SignListSerializer(serializers.ModelSerializer):
    studentName=serializers.ReadOnlyField(source='student.name')
    studentId=serializers.ReadOnlyField(source='student.stuId')
    class Meta:
        model= Sign
        fields=('studentName','studentId','signTime')



class CourseSignListSerializer(serializers.ModelSerializer):
    sign=SignSerializer(many=True)
    signNum=serializers.SerializerMethodField()
    class Meta:
        model=Course
        fields=('id','sign')

    def get_signNum(self,obj):
        return obj.sign.all().count()
