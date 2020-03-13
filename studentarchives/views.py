from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from studentarchives.models import StudentArchives
from studentarchives.serializers import StudentArchivesSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = StudentArchives.objects.all()
    serializer_class = StudentArchivesSerializer


class StudentDetail(APIView):

    def get_object(self, matrikel_number):
        try:
            return StudentArchives.objects.get(matrikel_number=matrikel_number)
        except StudentArchives.DoesNotExist:
            raise Http404

    def get(self, request, matrikel_number, format=None):
        students = self.get_object(matrikel_number)
        serializer = StudentArchivesSerializer(students)
        return Response(serializer.data)
