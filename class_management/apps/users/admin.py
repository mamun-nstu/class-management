from django.contrib import admin

# Register your models here.
from users.models import (
    Student,
    Instructor,
    Batch
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('email', 'student_id', 'batch', 'password', 'first_name', 'last_name', 'full_name', 'date_joined')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    fields = ('email', 'password', 'first_name', 'last_name', 'full_name', 'date_joined')


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    ordering = ('-start', 'active')