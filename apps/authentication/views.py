from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response
from apps.authentication.models import User
from apps.authentication.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = (permissions.AllowAny,)
  serializer_class = RegisterSerializer