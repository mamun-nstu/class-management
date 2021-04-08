from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CHOICES = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('admin', 'Admin'),
)


class CustomUsers(User):
    full_name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        choices=CHOICES
    )


class Student(CustomUsers):
    student_id = models.CharField(max_length=25, db_index=True, default='1')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.type = 'student'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.student_id}: {self.full_name}'

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'