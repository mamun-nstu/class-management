from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.utils.functional import cached_property

from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from google.oauth2 import id_token
from google.auth.transport import requests

from core.models import Course, Attendance
from core.serializers import CourseSearializer, AttendanceSerializer, GenericStudentSerializer
from core.utils import get_user_from_username, UserJWT
from users.models import Batch, Student, Instructor
from users.permission import IsInstructor, IsAdmin



@permission_classes([permissions.IsAdminUser,])
class Test(APIView):
    def get(self, request):
        return Response(status=200)


@permission_classes([IsInstructor])
class AttendanceView(APIView):
    def _create_default_attendace(self, student_id, course_id, date):
        return {
            "student": GenericStudentSerializer(Student.objects.get(id=student_id)).data,
            "date": date,
            "present": False,
            "course": course_id,
            "instructor": 1
        }
    
    @cached_property
    def instrutor(self):
        return self.request.app_user.user
    
    def get(self, request, batch, course, date):
        batch_data = Batch.objects.get(id=batch)
        # students = Student.objects.filter(batch=batch, courses__in=[course])
        students = Student.objects.filter(batch=batch)
        # to ensure that this course is taken by this instructor
        course = Course.objects.get(id=course, instructors__in=[self.instrutor])
        attendances = []
        for student in students:
            attendance = Attendance.objects.filter(student=student, course=course, date=date, instructor=self.instrutor)
            if attendance:
                attendances.append(AttendanceSerializer(attendance[0]).data)
            else:
                attendances.append(self._create_default_attendace(student_id=student.id, course_id=course.id, date=date))
        
        return Response(attendances, status=200)
    
    def _get_attendance_data(self, data):
        # to ensure that this course is taken by this instructor
        course = Course.objects.get(id=data.get("course"), instructors__in=[self.instrutor])
        return {
            "course_id": course.id,
            "date": data.get("date"),
            "instructor_id": self.instrutor.id,
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


@permission_classes([IsAdmin])
class CourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSearializer


@permission_classes([IsAdmin])
class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSearializer


@permission_classes([])
class CreateSessionView(APIView):
    def post(self, request):
        token = request.data.get('token')
        client_id = getattr(settings, 'GOOGLE_CLIENT_ID')
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            userid = idinfo['sub']
            username = idinfo.get('email')
            user = get_user_from_username(username=username)
            if not user:
                return Response({'error': 'user not found'}, status=404)
            token = UserJWT.generate_jwt(user)
            response = Response({'token': token}, status=200)
            response.set_cookie('auth_token', token, path='/')
            return response
        except Exception as e:
            # Invalid token
            pass
        return Response(status=400)


from django.core.files.storage import FileSystemStorage


@permission_classes([IsAdmin])
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


@permission_classes([])
class AppInfo(APIView):
    def get(self, request):
        data = {
            'total_students': Student.objects.count(),
            'total_instructors': Instructor.objects.count(),
            'total_courses': Course.objects.count(),
            'total_batches': Batch.objects.count()
        }
        return Response(data, status=200)

