from rest_framework import serializers

from core.serializers import CourseSearializer, GenericStudentSerializer
from users.models import (
    Student,
    Instructor, Batch
)


class StudentSerializer(GenericStudentSerializer):
    courses = CourseSearializer(many=True)

    def create(self, validated_data):
        courses = validated_data.pop('courses', [])
        instance = Student.objects.create(**validated_data)
        # Assignment.objects.create(Order=order, Equipment=instance)
        return instance

    def update(self, instance, validated_data):
        courses = validated_data.pop('courses', [])
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'username', 'first_name', 'last_name']


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
