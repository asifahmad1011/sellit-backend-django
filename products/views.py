from django.shortcuts import render
from rest_framework import generics, permissions
from products.models import Products
from products.serializers import ProductsSerializer
from products.permissions import IsOwnerOrReadOnly


# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class ProductsBySeller(generics.ListAPIView):
    serializer_class = ProductsSerializer

    # lookup_url_kwarg = "seller_id"

    def get_queryset(self):
        # seller_id = self.kwargs.get(self.lookup_url_kwarg)
        seller_id = self.kwargs['seller_id']
        queryset = Products.objects.filter(seller_id=seller_id)
        return queryset
