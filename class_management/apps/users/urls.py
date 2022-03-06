from django.urls import re_path

from users.views import (
    StudentAPI,
    StudentList,
    StudentDetail,
    InstructorList,
    InstructorDetail,
    BatchDetail,
    BatchList,
    StudentDashBoardView, InstructorDashboardView
)

app_name = 'users'

urlpatterns = [
    re_path(r'^students/(?P<pk>\d+)/$', StudentDetail.as_view(), name='student_detail'),
    re_path(
        r'^students/(?P<student_id>\d+)/courses/(?P<course_id>\d+)/attendances/$',
        StudentDashBoardView.get_course_attendances,
        name='student_dashboard_course_attendances'
    ),
    re_path(
        r'^students/(?P<student_id>\d+)/attendance_summary/$',
        StudentDashBoardView.get_attendance_summary,
        name='student_dashboard_attendance_summary'
    ),
    re_path(r'^students/$', StudentList.as_view(), name='student_list'),
    re_path(r'^instructors/(?P<pk>\d+)/$', InstructorDetail.as_view(), name='instructor_detail'),
    re_path(r'^instructors/$', InstructorList.as_view(), name='instructor_list'),
    re_path(
        r'^instructors/(?P<instructor_id>\d+)/courses/(?P<course_id>\d+)/summary/$',
        InstructorDashboardView.get_attendances,
        name='instructor_dashboard_attendance_summary'
    ),
    re_path(
        r'^instructors/(?P<instructor_id>\d+)/courses/(?P<course_id>\d+)/students/$',
        InstructorDashboardView.get_course_students,
        name='instructor_dashboard_course_students'
    ),
re_path(
        r'^instructors/(?P<instructor_id>\d+)/courses/(?P<course_id>\d+)/students/(?P<student_id>\d+)/attendances$',
        InstructorDashboardView.get_course_student_summary,
        name='instructor_dashboard_course_student_summary'
    ),
    re_path(r'^batches/(?P<pk>\d+)/$', BatchDetail.as_view(), name='batch_detail'),
    re_path(r'^batches/$', BatchList.as_view(), name='batch_list'),

]
