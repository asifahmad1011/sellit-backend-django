from rest_framework import serializers
from category.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'parent_id', 'created_date', 'modified_date']
