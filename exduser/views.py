from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from exduser.models import ExtendUser
from exduser.serializers import ExtendUserSerializer


class ExtendUserList(generics.ListCreateAPIView):
    queryset = ExtendUser.objects.all()
    serializer_class = ExtendUserSerializer


class ExtendUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExtendUser.objects.all()
    serializer_class = ExtendUserSerializer

