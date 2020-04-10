from rest_framework import serializers

from products.models import Products

from images.serializers import ImageSerializer

from images.models import Images


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['product_id', 'name', 'description', 'price', 'seller_id', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date']


class ProductsViewSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Products
        fields = ['product_id', 'name', 'description', 'price', 'seller_id', 'more_details', 'status',
                  'category', 'brand', 'product_condition', 'created_date', 'modified_date', 'images']




    # def create(self, validated_data):
    #     images_data = validated_data.pop('images')
    #     print("test data", **validated_data)
    #     product = Products.objects.create(**validated_data)
    #     for image_data in images_data:
    #         Images.objects.create(product=product, **image_data)
    #     return product


    # def create(self, validated_data):
    #     print("test data", validated_data)
    #     product = Products.objects.create(**validated_data)
    #     product1 = Products.objects.get()[-1]
    #     images_data = validated_data.pop('images')
    #     for image_data in images_data:
    #         image_data.product = product1.product_id
    #         Images.objects.create(product=product1.product_id, **image_data)
    #     return product

    # def create(self, validated_data):
    #     return Products.objects.create(**validated_data)
    #     # img = self.images.objects.get(product=self.product_id, image=self.images.image, url=self.images.url,
    #     #                               primary_image_id=0)
    #     # self.images.add(img)
    #     # return self
    #
    # def update(self, instance, validated_data):
    #     # instance.images = validated_data.get('images', instance.images)
    #     product1 = Products.objects.filter("-created_date")
    #     img = self.images.objects.get(product=product1.product_id, image=self.images.image, url=self.images.url,
    #                                   primary_image_id=0)
    #     product1.images.add(img)
    #     # self.images.add(img)
    #     # instance.images.product = validated_data.get('product_id', instance.product_id)
    #     # instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance

    # def create(self, validated_data):
    #     return Products.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     # instance.images = validated_data.get('images', instance.images)
    #     product1 = Products.objects.get()[-1]
    #     instance.images.product = validated_data.get('product_id', instance.product_id)
    #     # instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance
