from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.serializers import CourseSearializer, GenericStudentSerializer
from users.models import (
    Student,
    Instructor, Batch
)


class StudentSerializer(GenericStudentSerializer):
    courses = CourseSearializer(many=True, required=False, default=[])


class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSearializer(many=True, required=False, default=[])
    
    class Meta:
        model = Instructor
        fields = ['id', 'username', 'full_name', 'courses']


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
