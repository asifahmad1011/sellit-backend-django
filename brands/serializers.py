from rest_framework import serializers
from brands.models import Brands


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brands
        fields = ['id', 'category', 'brand_name', 'created_date', 'modified_date']