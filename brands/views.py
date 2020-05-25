from django.shortcuts import render
from rest_framework import generics
from brands.models import Brands
from brands.serializers import BrandsSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BrandsList(generics.ListAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


class BrandsCreate(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


class BrandsDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
