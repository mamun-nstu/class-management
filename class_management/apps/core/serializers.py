from rest_framework import serializers

from core.models import (
    Course,
    Attendance
)
from users.models import (
    Student,
    Instructor
)


class GenericStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['password']



class CourseSearializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    student = GenericStudentSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'
