from django.shortcuts import render
from rest_framework import generics
from brands.models import Brands
from brands.serializers import BrandsSerializer


class BrandsList(generics.ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


class BrandsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
