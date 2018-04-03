from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from django.core import serializers
from rest_framework import mixins
# from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Course, Sign, SignDetail
from django.db import connection
from .serializers import CourseUpdateSerializer, CourseRetrieveSerializer, \
    CourseCreateSerializer, TeacherCourseSerializer, \
    SignSerializer, SignCreateSerializer, SignDetailCreateSerializer, \
    SignSignDetailSerializer, CourseSignSerializer

# 获取自定义User
User = get_user_model()

'''
课程 创建 获取单个信息 更新
'''


class CourseViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Course.objects.all()
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        if self.action == 'create':
            return CourseCreateSerializer
        elif self.action == 'update' or self.action == 'partial_update':
            return CourseUpdateSerializer
        elif self.action == 'retrieve':
            return CourseRetrieveSerializer


"""
老师课程表 获取当个老师的课程列表
"""


class TeacherCourseViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = TeacherCourseSerializer

    def get_queryset(self):
        return User.objects.filter(userType='teacher')


'''
签到 创建
'''


class SignViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = SignCreateSerializer
    queryset = Sign.objects.all()


'''
课程签到列表 获取某个课程个的签到列表
'''


class CourseSignViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = CourseSignSerializer
    queryset = Course.objects.all()


"""
签到详情 创建
"""


class SignDetailViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = SignDetailCreateSerializer
    queryset = SignDetail.objects.all()


"""
签到的签到详情 获取谋次签到的签到详情
"""


class SignSignDetailViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Sign.objects.all()
    serializer_class = SignSignDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        sign_id = instance.id
        serializer = self.get_serializer(instance)
        signObjs = SignDetail.objects.filter(sign_id=sign_id, student_id__in=User.objects.filter(userType='student').values('id'))
        nonsignObjs = User.objects.filter(userType='student').exclude(id__in=SignDetail.objects.filter(sign_id=sign_id).values('student_id'))
        signList = []
        nonsignList = []
        for signObj in signObjs:
            queryDict = {}
            queryDict['signTime'] = signObj.signTime
            queryDict['signKind'] = signObj.signKind
            queryDict['id'] = signObj.student.id
            queryDict['stuId'] = signObj.student.stuId
            queryDict['name'] = signObj.student.name
            signList.append(queryDict)

        for nonsignObj in nonsignObjs:
            queryDict = {}
            queryDict['id'] = nonsignObj.id
            queryDict['stuId'] = nonsignObj.stuId
            queryDict['name'] = nonsignObj.name
            nonsignList.append(queryDict)

        queryDict = {}
        queryDict['signNum'] = len(signList)
        queryDict['nonsignNum']=len(nonsignList)
        queryDict['signList'] = signList
        queryDict['nonsignList']=nonsignList

        return Response(queryDict)
