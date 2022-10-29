from rest_framework import viewsets, status
from .models import Test
from .serializer import TestSeria
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


class TestView(viewsets.ModelViewSet):
    serializer_class = TestSeria
    queryset = Test.objects.all()
