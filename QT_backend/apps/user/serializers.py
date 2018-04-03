from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# 获取自定义User
User = get_user_model()


class StudentRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[
                                         UniqueValidator(queryset=User.objects.all(), message="用户已经存在")
                                     ])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )
    stuId = serializers.CharField(label="学号", help_text="学号", required=True, allow_blank=False,
                                     validators=[
                                         UniqueValidator(queryset=User.objects.all(), message="学号已经存在")
                                     ])
    userType = serializers.HiddenField(
        default='student'
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'userType', 'stuId')

    def create(self, validated_data):
        user = super(StudentRegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class TeacherRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[
                                         UniqueValidator(queryset=User.objects.all(), message="用户已经存在")
                                     ])

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    userType = serializers.HiddenField(
        default='teacher'
    )
    workId = serializers.CharField(label="教工号", help_text="教工号", required=True, allow_blank=False,
                                     validators=[
                                         UniqueValidator(queryset=User.objects.all(), message="教工号已经存在")
                                     ])
    class Meta:
        model = User
        fields = ('username', 'password', 'userType', 'workId')

    def create(self, validated_data):
        user = super(TeacherRegisterSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_userType(self):
        return 'teacher'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'telephone', 'name', 'workId')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'telephone', 'name', 'stuId')
