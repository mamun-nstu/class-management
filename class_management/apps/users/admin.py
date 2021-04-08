from django.contrib import admin

# Register your models here.
from users.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass