from django.contrib.auth.models import User
from django.db import models
from brands.models import Brands
from category.models import Category


# Create your models here.


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    slug = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seller = models.ForeignKey(User, related_name='seller_id', on_delete=models.CASCADE)
    more_details = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    product_condition = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # search_fields = ['name']
    # images = models.ManyToManyField(Images)

    def __str__(self):
        return self.name
