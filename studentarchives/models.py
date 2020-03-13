from django.db import models


# Create your models here.


class StudentArchives(models.Model):
    matrikel_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateTimeField()
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=6)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # def dateOfBirth(self):
    #     return self.dob.strftime('%B %d %Y')
