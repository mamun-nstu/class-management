from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import Student, Instructor, Batch
from users.serializers import StudentSerializer, InstructorSerializer, BatchSerializer
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
)


@permission_classes((permissions.AllowAny,))
class StudentList(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        req = self.request
        batch = req.GET.get('batch')
        course = req.GET.get('course')
        query = {
            'batch': batch,
        }
        if course:
            query.update({'courses__in': [course]})
        queryset = Student.objects.filter(**query)
        return queryset


@permission_classes((permissions.AllowAny,))
class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


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

