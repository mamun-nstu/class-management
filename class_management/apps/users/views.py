from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.utils import timezone
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Course, Attendance, CourseInstructors
from core.serializers import AttendanceSerializer, CourseSearializer
from core.utils import get_user_from_username, UserJWT
from users.models import Student, Instructor, Batch
from users.permission import IsStudent, IsInstructor, IsAdmin
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
    @permission_classes([IsStudent])
    def get_student(request):
        return Response(StudentSerializer(instance=request.app_user.user).data, status=200)
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsStudent])
    def get_course_attendances(request, course_id):
        student_id = request.app_user.user.id
        attendances = Attendance.objects.filter(course_id=course_id, student_id=student_id)
        attendances = AttendanceSerializer(attendances, many=True)
        return Response(attendances.data, status=200)
    
    @staticmethod
    def get_course_title(course_code, course_name):
        return f'{course_code} - {course_name}'
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsStudent])
    def get_attendance_summary(request):
        student_id = request.app_user.user.id
        attendances = Attendance.objects.filter(student_id=student_id).prefetch_related('course')
        total_classes = {}
        total_attendances = {}
        for attendance in attendances:
            course_title = StudentDashBoardView.get_course_title(attendance.course.code, attendance.course.name)
            total_classes[course_title] = total_classes.get(course_title, 0) + 1
            total_attendances[course_title] = total_attendances.get(course_title, 0) + (1 if attendance.present else 0)
        
        res = []
        for key, val in total_classes.items():
            total_class = val or 0
            total_present = total_attendances.get(key, 0)
            res.append({
                'course_title': key,
                'total_class': total_class,
                'total_present': total_present,
                'percentage': round(total_present / total_class, 2)
            })
        return Response(res, status=200)


@permission_classes([IsAdmin])
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
        image = student_data.pop('image', None)
        serializer = self.serializer_class(data=student_data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('courses', [])
            student = Student.objects.create(**validated_data)
            if image:
                student.image = image
                student.save()
            for course in courses:
                student.courses.add(Course.objects.get(id=course.get('id')))
            
            return Response(self.serializer_class(student).data, status=200)
        return Response(serializer.errors, status=400)


@permission_classes([IsAdmin])
class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def put(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        student_data = request.data
        # nested data problem in serializer
        courses = student_data.pop('courses', [])
        image = student_data.pop('image', None)
        student = Student.objects.get(id=id)
        serializer = self.serializer_class(data=student_data, instance=student)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('courses', [])
            for (key, value) in validated_data.items():
                setattr(student, key, value)
            if image:
                student.image = image
            student.save()
            student.courses.clear()
            for course in courses:
                student.courses.add(Course.objects.get(id=course.get('id')))
            
            return Response(self.serializer_class(student).data, status=200)
        return Response(serializer.errors, status=400)


@permission_classes([IsAdmin])
class InstructorList(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    
    def post(self, request, *args, **kwargs):
        instructor_data = request.data
        # nested data problem in serializer
        courses = instructor_data.pop('courses', [])
        image = instructor_data.pop('image', None)
        serializer = self.serializer_class(data=instructor_data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('courses', [])
            instructor = Instructor.objects.create(**validated_data, image=image)
            batch = Batch.objects.all()
            batch = batch[0]
            for course in courses:
                ci = CourseInstructors(
                    course=Course.objects.get(id=course.get('id')),
                    instructor=instructor,
                    batch=batch,
                    start=timezone.now()
                )
                ci.save()
            
            return Response(self.serializer_class(instructor).data, status=200)
        return Response(serializer.errors, status=400)


@permission_classes([IsAdmin])
class InstructorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    
    def put(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        instructor_data = request.data
        image = instructor_data.pop('image', None)
        # nested data problem in serializer
        courses = instructor_data.pop('courses', [])
        instructor = Instructor.objects.get(id=id)
        serializer = self.serializer_class(data=instructor_data, instance=instructor)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            validated_data.pop('courses', [])
            for (key, value) in validated_data.items():
                setattr(instructor, key, value)
            if image:
                instructor.image = image
            instructor.save()
            instructor.courses.clear()
            batch = Batch.objects.all()
            batch = batch[0]
            for course in courses:
                ci = CourseInstructors(
                    course=Course.objects.get(id=course.get('id')),
                    instructor=instructor,
                    batch=batch,
                    start=timezone.now()
                )
                ci.save()
            
            return Response(self.serializer_class(instructor).data, status=200)
        return Response(serializer.errors, status=400)


class InstructorDashboardView:
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsInstructor])
    def get_instructor(request):
        return Response(InstructorSerializer(instance=request.app_user.user).data, status=200)
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsInstructor])
    def get_courses(request):
        instructor_id = request.app_user.user.id
        courses = Course.objects.filter(courseinstructors__instructor__id=instructor_id).all()
        return Response(CourseSearializer(instance=courses, many=True).data, status=200)
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsInstructor])
    def get_attendances(request, course_id):
        instructor_id = request.app_user.user.id
        total_classes = Attendance.objects \
            .filter(course_id=course_id, instructor_id=instructor_id) \
            .values('date') \
            .distinct() \
            .count()
        attendances = Attendance.objects \
            .filter(course_id=course_id, instructor_id=instructor_id) \
            .prefetch_related('student')
        student_info = {}
        total_present = {}
        for attendance in attendances:
            student = attendance.student
            student_info[student.id] = student
            total_present[student.id] = total_present.get(student.id, 0) + (1 if attendance.present else 0)
        res = []
        
        for _id, student in student_info.items():
            presents = total_present.get(_id, 0)
            res.append({
                'student_id': student.student_id,
                'student_name': student.full_name,
                'total_present': presents,
                'percentage': round(presents / total_classes * 100, 2),
                'total_classes': total_classes
            })
        return Response(res, status=200)
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsInstructor])
    def get_course_students(request, course_id):
        instructor = request.app_user.user
        course = Course.objects.get(id=course_id, instructors__in=[instructor])
        students = Student.objects.filter(courses__in=[course])
        return Response(StudentSerializer(instance=students, many=True).data, status=200)
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes([IsInstructor])
    def get_course_student_summary(request, course_id, student_id):
        instructor_id = request.app_user.user.id
        attendances = Attendance.objects.filter(student_id=student_id, instructor_id=instructor_id, course_id=course_id)
        total_classes = attendances.count()
        res = []
        present = 0
        for attendance in attendances:
            res.append({
                'date': attendance.date,
                'present': attendance.present
            })
            present += 1 if attendance.present else 0
        
        percentage = 0
        if total_classes:
            percentage = round(present / total_classes * 100, 2)
        return Response({
            'classes': res,
            'total_classes': total_classes,
            'total_present': present,
            'percentage': percentage
        }, status=200
        )


@permission_classes((permissions.AllowAny,))
class BatchList(ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


@permission_classes((permissions.AllowAny,))
class BatchDetail(RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


@permission_classes((permissions.AllowAny,))
class UserView(APIView):
    queryset = Batch.objects.all()
    
    def get(self, request):
        return Response(request.app_user.dict(), status=200)


@permission_classes((permissions.AllowAny,))
class GetToken(APIView):
    def get(self, request):
        username = request.query_params.get('username', '')
        user = get_user_from_username(username=username)
        if not user:
            return Response({'error': 'user not found'}, status=404)
        token = UserJWT.generate_jwt(user)
        response = Response({'token': token}, status=200)
        response.set_cookie('auth_token', token, path='/')
        return response


@permission_classes([IsAdmin])
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
