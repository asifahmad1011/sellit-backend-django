from rest_framework import serializers

from products.models import Products


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'seller_id', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date']
