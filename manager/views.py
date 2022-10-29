from rest_framework import viewsets, status
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import viewsets
from manager.serializer import *
from manager.models import *


class Permission_View(viewsets.ModelViewSet):
    serializer_class = Permission_Serializer
    queryset = PermissionModel.objects.all()
    filterset_fields = ['user']


class Register(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        username = request.data['username']
        email = request.data['email']
        passw = request.data['password']

        if username and email and passw:
            if User.objects.filter(username=username).values().exists():
                return Response({"error": "user alredy exist"}, status=status.HTTP_400_BAD_REQUEST)
            elif User.objects.filter(email=email).values().exists():
                return Response({"error": "email alredy exist"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                a = User(username=request.data['username'], email=email, password=make_password(
                    password=passw))
                a.save()
            return Response("Registration success", status=status.HTTP_201_CREATED)
        else:
            raise ValidationError(
                {"field_error": "username,emial,password is required !!"}, status=status.HTTP_400_BAD_REQUEST)
