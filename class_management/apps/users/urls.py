from django.urls import re_path

from users.views import (
    StudentAPI,
    StudentList,
    StudentDetail,
    InstructorList,
    InstructorDetail, BatchDetail, BatchList
)

app_name = 'users'

urlpatterns = [
    re_path(r'^students/(?P<pk>\d+)/$', StudentDetail.as_view(), name='student_detail'),
    re_path(r'^students/$', StudentList.as_view(), name='student_list'),
    re_path(r'^instructors/(?P<pk>\d+)/$', InstructorDetail.as_view(), name='instructor_detail'),
    re_path(r'^instructors/$', InstructorList.as_view(), name='instructor_list'),
    re_path(r'^batches/(?P<pk>\d+)/$', BatchDetail.as_view(), name='batch_detail'),
    re_path(r'^batches/$', BatchList.as_view(), name='batch_list'),

]
