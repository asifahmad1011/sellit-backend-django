from rest_framework import serializers

from products.models import Products

from images.serializers import ImageSerializer

from images.models import Images


class ProductsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Products
        fields = ['product_id', 'name', 'description', 'price', 'seller_id', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        print("test data", **validated_data)
        product = Products.objects.create(**validated_data)
        for image_data in images_data:
            Images.objects.create(product=product, **image_data)
        return product

    # def update(self):
