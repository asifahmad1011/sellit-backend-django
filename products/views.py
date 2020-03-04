from django.shortcuts import render
from rest_framework import generics
from products.models import Products
from products.serializers import ProductsSerializer


# Create your views here.


class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsBySeller(generics.ListAPIView):
    serializer_class = ProductsSerializer

    # lookup_url_kwarg = "seller_id"

    def get_queryset(self):
        # seller_id = self.kwargs.get(self.lookup_url_kwarg)
        seller_id = self.kwargs['seller_id']
        queryset = Products.objects.filter(seller_id=seller_id)
        return queryset
