"""
URL configuration for course_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from courses.views import create_category, create_course, create_student, enroll_student

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", create_category, name="create_category"),
    path("create-course/", create_course, name="create_course"),
    path("create-student/", create_student, name="create_student"),
    path("create-enrollment/", enroll_student, name="create_enrollment"),
]
