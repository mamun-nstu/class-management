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
        fields = '__all__'


class CourseSearializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class GenericAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    student = GenericStudentSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'
        
