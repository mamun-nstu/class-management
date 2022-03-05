from django.db import models

# Create your models here.
from users.models import Instructor, Batch, Student


class Course(models.Model):
    code = models.CharField(max_length=12, db_index=True, unique=True)
    name = models.CharField(max_length=25, unique=True)
    active = models.BooleanField(default=True)
    instructors = models.ManyToManyField(Instructor, null=True, blank=True, through='CourseInstructors', related_name='courses')
    students = models.ManyToManyField(Student, null=True, blank=True, related_name='courses')

    def __str__(self):
        return f'{self.code}: {self.name}'


class CourseInstructors(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, db_index=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, db_index=True)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.course.code}: {self.instructor.full_name} ({self.batch})'


class Notice(models.Model):
    message = models.TextField(max_length=20000)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student.student_id}: {self.issue_date}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    present = models.BooleanField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.student.full_name}: {self.date}'

    class Meta:
        unique_together = ('date', 'course', 'student')