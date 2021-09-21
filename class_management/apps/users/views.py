from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Course, Attendance
from core.serializers import AttendanceSerializer
from users.models import Student, Instructor, Batch
from users.serializers import StudentSerializer, InstructorSerializer, BatchSerializer
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
)


class StudentDashBoardView:
    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def get_course_attendances(request, student_id, course_id):
        attendances = Attendance.objects.filter(course_id=course_id, student_id=student_id)
        attendances = AttendanceSerializer(attendances, many=True)
        return Response(attendances.data, status=200)



@permission_classes((permissions.AllowAny,))
class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        req = self.request
        batch = req.GET.get('batch')
        course = req.GET.get('course')
        query = {}
        if batch:
            query.update({'batch': batch})
        if course:
            query.update({'courses__in': [course]})
        queryset = Student.objects.filter(**query)
        return queryset

    def post(self, request, *args, **kwargs):
        student_data = request.data
        # nested data problem in serializer
        courses = student_data.pop('courses', [])
        serializer = self.serializer_class(data=student_data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('courses', [])
            student = Student.objects.create(**validated_data)
            for course in courses:
                student.courses.add(Course.objects.get(id = course.get('id')))

            return Response(self.serializer_class(student).data, status=200)
        return Response(serializer.errors, status=400)


@permission_classes((permissions.AllowAny,))
class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        student_data = request.data
        # nested data problem in serializer
        courses = student_data.pop('courses', [])
        student = Student.objects.get(id=id)
        serializer = self.serializer_class(data=student_data, instance=student)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('courses', [])
            for (key, value) in validated_data.items():
                setattr(student, key, value)
            student.save()
            student.courses.clear()
            for course in courses:
                student.courses.add(Course.objects.get(id = course.get('id')))

            return Response(self.serializer_class(student).data, status=200)
        return Response(serializer.errors, status=400)


@permission_classes((permissions.AllowAny,))
class InstructorList(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


@permission_classes((permissions.AllowAny,))
class InstructorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


@permission_classes((permissions.AllowAny,))
class BatchList(ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


@permission_classes((permissions.AllowAny,))
class BatchDetail(RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


@permission_classes((permissions.AllowAny,))
class StudentAPI(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Response('student not found', 404)

    def get(self, request, pk=None, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def post(self, request):
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response('created', status=200)
    #     return Response(serializer.errors, status=400)
    #
    # def put(self, request):
    #     id = request.data.get('id')
    #     student = Student.objects.get(id=id)
    #     serializer = StudentSerializer(student, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response('updated', status=200)
    #     return Response(serializer.errors, status=400)
    #
    # def get(self, request):
    #     students = StudentSerializer(Student.objects.all().values(), many=True)
    #     return Response(students.data, status=200)
