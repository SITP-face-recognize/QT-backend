from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Course, Sign, SignDetail
from user.serializers import StudentSerializer
# 获取自定义User
User = get_user_model()


class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('courseName', 'courseInfo')


class CourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'courseName', 'courseInfo')


class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'courseName', 'courseInfo', 'student', 'teacher')

class CourseStudentListSerializer(serializers.ModelSerializer):
    student=StudentSerializer(many=True)
    class Meta:
        model=Course
        fields=('student',)


class TeacherCourseSerializer(serializers.ModelSerializer):
    teacher_course = CourseRetrieveSerializer(many=True)

    class Meta:
        model = User
        fields = ('teacher_course',)


class SignDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignDetail
        fields = ('sign', 'student', 'signKind')


class SignCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = ('id', 'course')


class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = ('id', 'signTime')


class CourseSignSerializer(serializers.ModelSerializer):
    course_sign = SignSerializer(many=True)

    class Meta:
        model = Course
        fields = ('course_sign',)


class SignDetailSerializer(serializers.ModelSerializer):
    studentName = serializers.ReadOnlyField(source='student.name')
    studentId=serializers.ReadOnlyField(source='student.id')
    class Meta:
        model = SignDetail
        fields = ('signTime', 'studentName','studentId')


class SignSignDetailSerializer(serializers.ModelSerializer):
    sign_signDetail = SignDetailSerializer(many=True)

    class Meta:
        model = Sign
        fields = ('sign_signDetail',)
