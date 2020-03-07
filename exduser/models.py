from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matrikel_number = models.IntegerField(primary_key=True)
    dob = models.DateTimeField()
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=6)
    # role = models.ForeignKey(Roles, models.DO_NOTHING)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ExtendUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.save()
    # print(instance)