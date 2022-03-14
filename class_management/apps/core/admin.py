from django.contrib import admin

# Register your models here.
from core.models import Course, CourseInstructors, Notice, Attendance


class CourseInline(admin.TabularInline):
    model = Course.instructors.through
    ordering = ('active',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        CourseInline
    ]


@admin.register(CourseInstructors)
class CourseInstructorsAdmin(admin.ModelAdmin):
    ordering = ('active',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    ordering = ('-date', 'student')

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    ordering = ('-issue_date', )