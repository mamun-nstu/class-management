from django.contrib import admin

# Register your models here.
from users.models import (
    Student,
    Instructor,
    Batch
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('username', 'student_id', 'batch', 'full_name', 'date_joined')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    fields = ('username', 'full_name', 'date_joined')


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    ordering = ('-start', 'active')