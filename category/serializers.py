from category.models import Category
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'parent_id', 'created_date', 'modified_date')

    def create(self, validated_data):
        name = validated_data['name']
        description = validated_data['description']
        parent_id = validated_data['parent_id']
        category_obj = Category(
            name=name,
            description=description,
            parent_id=parent_id,
            )
        category_obj.save()
        return validated_data
