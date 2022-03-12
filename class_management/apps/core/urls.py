from django.urls import re_path

from .views import (
    AttendanceView,
    CourseDetail,
    CourseList,
    CreateSessionView,
    UploadUserImage,
    AppInfo,
)

urlpatterns = [
    re_path(r'^session/?$', CreateSessionView.as_view(), name='create_session'),
    re_path(r"^attendances/batches/(?P<batch>[\d]+)/courses/(?P<course>[\d]+)/date/(?P<date>[\d-]+)/?$",
            AttendanceView.as_view(),
            name="attendance"),

    re_path(r'^courses/(?P<pk>\d+)/$', CourseDetail.as_view(), name='course_detail'),
    re_path(r'^courses/(?P<pk>\d+)/$', CourseDetail.as_view(), name='course_detail'),
    re_path(r'^courses/$', CourseList.as_view(), name='course_list'),
    re_path(r'^upload-user-img/$', UploadUserImage.as_view(), name='upload_user_img'),
    re_path(r'^app-info/$', AppInfo.as_view(), name='app_info'),
    
]
