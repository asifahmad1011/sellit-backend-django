from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    parent_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    images = models.CharField(max_length=255, blank=True, null=True)