from django.db import models
from products.models import Products


# Create your models here.


class Images(models.Model):
    product = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    image_id = models.AutoField(primary_key=True)
    image = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    primary_image_id = models.IntegerField(blank=True, null=True)
    video = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['product', 'image_id']
        ordering = ['image_id']

        def __str__(self):
            return '%d: %s' % (self.image_id, self.image)
