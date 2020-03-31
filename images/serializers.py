from rest_framework import serializers
from images.models import Images


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['image_id', 'image', 'url', 'primary_image_id', 'product', 'video',
                  'created_date', 'modified_date']
