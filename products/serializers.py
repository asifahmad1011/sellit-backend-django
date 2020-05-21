from rest_framework import serializers

from products.models import Products

from images.serializers import ImageSerializer

from images.models import Images

from users.serializers import UserSerializer


class ProductsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'seller', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date', 'images']


class ProductsViewSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Products
        fields = ['product_id', 'name', 'description', 'price', 'seller', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date', 'images']


