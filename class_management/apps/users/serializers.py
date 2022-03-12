from rest_framework import serializers

from core.models import CourseInstructors
from core.serializers import CourseSearializer, GenericStudentSerializer
from users.models import (
    Instructor,
    Batch,
)


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


class StudentSerializer(GenericStudentSerializer):
    courses = CourseSearializer(many=True, required=False, default=[])
    batch = BatchSerializer(required=False)


class InstructorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['full_name', 'username']


class CourseDetailSerializer(serializers.ModelSerializer):
    course = CourseSearializer()
    batch = BatchSerializer()
    
    class Meta:
        model = CourseInstructors
        fields = '__all__'


class InstructorSerializer(serializers.ModelSerializer):
    course_details = CourseDetailSerializer(many=True, required=False, default=[])
    
    class Meta:
        model = Instructor
        fields = ['id', 'username', 'full_name', 'courses', 'image', 'course_details']
