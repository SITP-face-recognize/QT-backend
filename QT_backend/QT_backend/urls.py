"""QT_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url, include
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from user.views import StudentViewset, TeacherViewset
from course.views import CourseViewset,TeacherCourseViewset,SignViewset,CourseSignViewset,SignDetailViewset,SignSignDetailViewset,CourseStudentViewset
router = DefaultRouter()

router.register(r'student', StudentViewset, base_name="student")

router.register(r'teacher', TeacherViewset, base_name="teacher")

router.register(r'course', CourseViewset, base_name="course")

router.register(r'sign', SignViewset, base_name="sign")

router.register(r'signDetail', SignDetailViewset, base_name="signDetail")

router.register(r'teacherCourse', TeacherCourseViewset, base_name="teacherCourse")

router.register(r'courseSign', CourseSignViewset, base_name="courseSign")

router.register(r'signSignDetail', SignSignDetailViewset, base_name="signSignDetail")

router.register(r'courseStudent', CourseStudentViewset, base_name="courseStudent")

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='My API title')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),

    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),

    # drf 自带auth
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt auth
    url(r'^login/', obtain_jwt_token),

]
