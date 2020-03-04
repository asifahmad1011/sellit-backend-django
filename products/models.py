from django.db import models
from brands.models import Brands
from category.models import Category

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=45)
    slug = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seller_id = models.IntegerField()
    more_details = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    category = models.ForeignKey(Category, models.DO_NOTHING, null=True)
    brand = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    product_condition = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

