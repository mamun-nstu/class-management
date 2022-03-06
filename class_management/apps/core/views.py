from django.shortcuts import render

# Create your views here.

from django.conf import settings

from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from google.oauth2 import id_token
from google.auth.transport import requests

from core.models import Course, Attendance
from core.serializers import CourseSearializer, AttendanceSerializer, GenericStudentSerializer
from users.models import Batch, Student


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = 'Tahmid'
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class JWTToken():
    def __init__(self, token):
        self.token = Token(token, verify=False)

    @property
    def is_valid(self):
        try:
            self.token.verify()
            return True
        except Exception:
            return False

    @property
    def payload(self):
        return self.token.payload


@permission_classes((permissions.IsAdminUser,))
class Test(APIView):
    def get(self, request):
        return Response(status=200)


@permission_classes((permissions.AllowAny,))
class AttendanceView(APIView):
    def _create_default_attendace(self, student_id, course_id, date):
        return {
            "student": GenericStudentSerializer(Student.objects.get(id=student_id)).data,
            "date": date,
            "present": False,
            "course": course_id,
            "instructor": 1
        }

    def get(self, request, batch, course, date):
        batch_data = Batch.objects.get(id=batch)
        # students = Student.objects.filter(batch=batch, courses__in=[course])
        students = Student.objects.filter(batch=batch)
        attendances = []
        for student in students:
            attendance = Attendance.objects.filter(student=student, course=course, date=date)
            if attendance:
                attendances.append(AttendanceSerializer(attendance[0]).data)
            else:
                attendances.append(self._create_default_attendace(student_id=student.id, course_id=course, date=date))

        return Response(attendances, status=200)

    def _get_attendance_data(self, data):
        return {
            "course_id": data.get("course"),
            "date": data.get("date"),
            # "instructor_id": data.get("instructor"),
            "student_id": data.get("student").get('id'),
            "present": data.get("present")
        }

    def put(self, request, batch, course, date):
        attendances = request.data
        for attendance in attendances:
            data = self._get_attendance_data(attendance)
            if attendance.get('id'):
                Attendance.objects.filter(id=attendance.get('id')).update(**data)
            else:
                Attendance.objects.create(**data)

        return Response(status=200)


@permission_classes((permissions.AllowAny,))
class CourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSearializer


@permission_classes((permissions.AllowAny,))
class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSearializer


@permission_classes((permissions.AllowAny,))
class CreateSessionView(APIView):
    def post(self, request):
        token = request.data.get('token')
        client_id = getattr(settings, 'GOOGLE_CLIENT_ID')
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            userid = idinfo['sub']
            username = idinfo.get('email')
            request.session['user'] = username
            return Response(status=200)
        except Exception as e:
            # Invalid token
            pass
        return Response(status=400)
    
from django.core.files.storage import FileSystemStorage


@permission_classes((permissions.AllowAny,))
class UploadUserImage(APIView):
    img_location = f'uploads/user-imgs'
    def post(self, request):
        file_obj = request.FILES['files']
        file_name = request.data.get('file_name', '')
        if file_name:
            file_name += '.' + file_obj.name.split('.')[-1]
        else:
            file_name = file_obj.name
        img_location = f'{settings.MEDIA_ROOT}/{self.img_location}'
        fs = FileSystemStorage(img_location)
        res = fs.save(file_name, file_obj)
        res = f'{self.img_location}/{res}'
        return Response({'upload_url': res}, status=200)
