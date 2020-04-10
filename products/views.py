import itertools

from django.shortcuts import render
from rest_framework import generics, status
from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from images.serializers import ImageSerializer


class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsBySeller(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer

    # lookup_url_kwarg = "seller_id"

    def get_queryset(self):
        # seller_id = self.kwargs.get(self.lookup_url_kwarg)
        seller_id = self.kwargs['seller_id']
        queryset = Products.objects.filter(seller_id=seller_id)
        return queryset
