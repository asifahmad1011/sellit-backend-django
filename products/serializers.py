from rest_framework import serializers

from products.models import Products

from images.serializers import ImageSerializer

from images.models import Images

from users.serializers import UserSerializer


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'seller', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date']


class ProductsViewSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Products
        fields = ('product_id', 'name', 'description', 'price', 'seller', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date', 'images')

    # def create(self, validated_data):
    #     images_data = validated_data.pop('images')
    #     product = Products.objects.create(**validated_data)
    #     for image_data in images_data:
    #         Images.objects.create(product=product, **image_data)
    #     return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images')
        images = instance.images.all()
        images = list(images)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.seller = validated_data.get('seller', instance.seller)
        instance.more_details = validated_data.get('more_details', instance.more_details)
        instance.status = validated_data.get('status', instance.status)
        instance.category = validated_data.get('category', instance.category)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.product_condition = validated_data.get('product_condition', instance.product_condition)

        instance.save()

        for image_data in images_data:
            image = images.pop(0)
            image.image = image_data.get('image', image.image)
            image.url = image_data.get('url', image.url)
            image.primary_image_id = image_data.get('primary_image_id', image.primary_image_id)
            image.video = image_data.get('video', image.video)
            image.save()
        return instance
