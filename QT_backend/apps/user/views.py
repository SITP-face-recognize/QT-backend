from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions
from .serializers import StudentRegisterSerializer, TeacherRegisterSerializer, TeacherSerializer, StudentSerializer

# 获取自定义User
User = get_user_model()

'''
 学生 注册 更新 获取单个信息
'''
class StudentViewset(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create" or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return []
        return []

    def get_serializer_class(self):
        if self.action == "create":
            return StudentRegisterSerializer
        elif self.action == "retrieve"or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return StudentSerializer

    def get_object(self):
        return self.request.user


"""
老师 注册 更新 获取当个信息
"""
class TeacherViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        elif self.action == "create" or self.action == 'update' or self.action == 'partial_update':
            return []
        return []

    def get_serializer_class(self):
        if self.action == "create":
            return TeacherRegisterSerializer
        elif self.action == "retrieve" or self.action == 'update' or self.action == 'partial_update':
            return TeacherSerializer

    def get_object(self):
        return self.request.user
