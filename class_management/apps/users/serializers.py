from rest_framework import serializers
from core.serializers import CourseSearializer, GenericStudentSerializer
from users.models import (
    Instructor,
    Batch,
)


class StudentSerializer(GenericStudentSerializer):
    courses = CourseSearializer(many=True, required=False, default=[])


class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSearializer(many=True, required=False, default=[])
    
    class Meta:
        model = Instructor
        fields = ['id', 'username', 'full_name', 'courses', 'image']


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
