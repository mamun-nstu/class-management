from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserType:
    STUDENT = 'student'
    INSTRUCTOR = 'instructor'
    ADMIN = 'admin'


CHOICES = (
    ('student', 'Student'),
    ('instructor', 'Instructor'),
    ('admin', 'Admin'),
)


class CustomUsers():
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    date_joined = models.DateField(null=True, blank=True)


class Batch(models.Model):
    name = models.CharField(max_length=25, unique=True, db_index=True)
    active = models.BooleanField(default=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'batches'


class Student(CustomUsers):
    student_id = models.CharField(max_length=25, db_index=True, unique=True, default='1')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.student_id}: {self.full_name}'

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Instructor(CustomUsers):

    def __str__(self):
        return f'{self.email}: {self.full_name}'

    class Meta:
        verbose_name = 'instructor'
        verbose_name_plural = 'instructors'
