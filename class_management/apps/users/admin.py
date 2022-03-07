from django.contrib import admin

# Register your models here.
from users.models import (
    Student,
    Instructor,
    Admin,
    Batch,
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('username', 'student_id', 'batch', 'full_name', 'date_joined', 'image_tag', 'image')
    readonly_fields = ['image_tag']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    fields = ('username', 'full_name', 'date_joined',  'image_tag', 'image')
    readonly_fields = ['image_tag']
    

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    fields = ('username', 'full_name', 'date_joined',  'image_tag', 'image')
    readonly_fields = ['image_tag']


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    ordering = ('-start', 'active')