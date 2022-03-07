from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import mark_safe


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


class CustomUsers(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    date_joined = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/user-imgs/')

    def image_tag(self):
        image = self.image
        if not image:
            return
        return mark_safe(f'<img src="{settings.MEDIA_URL}{image}" width="150" height="150" alt="Image not available" />')

    image_tag.short_description = 'Image Preview'


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
        return f'{self.username}: {self.full_name}'

    class Meta:
        verbose_name = 'instructor'
        verbose_name_plural = 'instructors'
        

class Admin(CustomUsers):

    def __str__(self):
        return f'{self.username}: {self.full_name}'
    
    def save(self, *args, **kwargs):
        admin_user = User.objects.filter(username=self.username)
        if not admin_user.count():
            User.objects.create_superuser(username=self.username)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'admin'
        verbose_name_plural = 'admins'
