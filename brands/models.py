from django.db import models
from category.models import Category

# Create your models here.


class Brands(models.Model):
    # category = models.ForeignKey('Category', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    brand_name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
