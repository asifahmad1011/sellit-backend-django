from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matrikel_number = models.IntegerField()
    dob = models.DateTimeField()
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=6)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.users.save()
