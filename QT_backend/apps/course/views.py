from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Course,Sign
from .serializers import SignSerializer,CourseSerializer,TeacherCourseListSerializer,CourseSignListSerializer

# 获取自定义User
Teacher = get_user_model()


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = CourseSerializer



class SignViewset(viewsets.ModelViewSet):
    queryset = Sign.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = SignSerializer

class TeacherCourseViewset(mixins.ListModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = TeacherCourseListSerializer

    def get_queryset(self):
        return self.request.user

class SignCourseViewset(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = CourseSignListSerializer
    queryset = Course.objects.all()

