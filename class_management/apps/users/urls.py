from django.urls import re_path

from users.views import (
    StudentAPI,
    StudentList,
    StudentDetail
)

app_name = 'users'

urlpatterns = [
    re_path(r'^students/(?P<pk>\d+)/$', StudentDetail.as_view(), name='student_detail'),
    re_path(r'^students/$', StudentList.as_view(), name='student_list'),

]
