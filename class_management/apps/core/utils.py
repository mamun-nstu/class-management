import jwt
from django.conf import settings

import logging

from core.serializers import CustomUserSerializer
from users.models import Student, Instructor, Admin

logger = logging.getLogger(__name__)


def get_user_from_username(username):
    student = Student.objects.filter(username=username)
    instructor = Instructor.objects.filter(username=username)
    admin = Admin.objects.filter(username=username)
    if student:
        student = student[0]
    if instructor:
        instructor = instructor[0]
    if admin:
        admin = admin[0]
    
    return student or instructor or admin


class UserJWT:
    algorithm = 'HS256'
    secret = settings.SECRET_KEY
    
    @staticmethod
    def get_user_info_for_token(user):
        return {
            'username': user.username,
            'id': user.id
        }
    
    @staticmethod
    def generate_jwt(user):
        encoded_jwt = jwt.encode(UserJWT.get_user_info_for_token(user), UserJWT.secret, algorithm=UserJWT.algorithm)
        return encoded_jwt
    
    @staticmethod
    def decode_jwt(token):
        try:
            decoded_val = jwt.decode(token, UserJWT.secret, algorithms=[UserJWT.algorithm])
            return decoded_val
        except Exception as e:
            logger.error(f'Error decoding jwt: {e}')
            return None
    
    class UserInfo:
        def __init__(self, student, instructor, admin):
            self.is_student = False
            self.is_instructor = False
            self.is_admin = False
            self.type = None
            if student:
                self.is_student = True
                self.type = 'student'
            if instructor:
                self.is_instructor = True
                self.type = 'instructor'
            if admin:
                self.is_admin = True
                self.type = 'admin'
            self.user = student or instructor or admin
            self.logged_in = bool(self.user)
            self.anonymous = not bool(self.user)
        
        def dict(self):
            res = {
                'type': self.type,
                'logged_in': self.logged_in,
                'anonymous': self.anonymous,
            }
            res.update(CustomUserSerializer(instance=self.user).data)
            return res
        
    @staticmethod
    def get_user(token):
        decoded_val = UserJWT.decode_jwt(token)
        if not decoded_val:
            return UserJWT.UserInfo(None, None, None)
        username = decoded_val.get('username')
        student = Student.objects.filter(username=username)
        instructor = Instructor.objects.filter(username=username)
        admin = Admin.objects.filter(username=username)
        if student:
            student = student[0]
        if instructor:
            instructor = instructor[0]
        if admin:
            admin = admin[0]
        return UserJWT.UserInfo(student, instructor, admin)
        # admin_user = CustomUsers.objects.get(username=decoded_val.get('username'))
