import itertools

from django.shortcuts import render
from rest_framework import generics, status, filters
from products.models import Products
from products.serializers import ProductsSerializer, ProductsViewSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from images.serializers import ImageSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsViewSerializer
    pagination_class = StandardResultsSetPagination


class ProductsListCreate(generics.CreateAPIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsViewSerializer

    def post(self, request, *args, **kwargs):
        image_data = request.data["images"]
        del request.data["images"]
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            last_product = Products.objects.latest("created_date")
            update_image_data = self.get_Image_data(image_data, last_product.product_id)
            for single_image_data in update_image_data:
                serializer_image = ImageSerializer(data=single_image_data)
                if serializer_image.is_valid():
                    serializer_image.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_Image_data(self, image_data, product_id):
        for single_image_data in image_data:
            single_image_data.update({"product": product_id})
        return image_data


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsViewSerializer


class ProductsBySeller(generics.ListAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = ProductsViewSerializer

    # lookup_url_kwarg = "seller_id"

    def get_queryset(self):
        # seller_id = self.kwargs.get(self.lookup_url_kwarg)
        seller_id = self.kwargs['seller_id']
        queryset = Products.objects.filter(seller_id=seller_id)
        return queryset


class ProductsByName(generics.ListAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductsViewSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    # lookup_url_kwarg = "seller_id"
    #
    # def get_queryset(self):
    #     # seller_id = self.kwargs.get(self.lookup_url_kwarg)
    #     name = self.kwargs['name']
    #     queryset = Products.objects.filter(name=name)
    #     return queryset

    # def get_queryset(self, *arg, **kwargs):
    #     queryset_list = Products.objects.all()
    #     query = self.request.GET.get("q")
    #     if query:
    #         queryset_list = queryset_list.filter(
    #             Q(name__icontains=query)
    #         ).distinct()
    #     return queryset_list
