from rest_framework import serializers

from users.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_id', 'username', 'first_name', 'last_name']
