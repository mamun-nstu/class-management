from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

@permission_classes((permissions.AllowAny,))
class StatusApi(APIView):
    def get(self, request):
        return Response("ok", status=200)