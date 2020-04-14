from django.shortcuts import render
from django.contrib.auth.models import User
from users.serializers import UserSerializer, UsersSerializer
from rest_framework import generics

# Create your views here.

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
