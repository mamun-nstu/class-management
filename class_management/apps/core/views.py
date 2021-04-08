from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView

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
