from django.contrib.auth.models import User
from django.db import models
from products.models import Products


# Create your models here.


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products, related_name='product', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='seller', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

