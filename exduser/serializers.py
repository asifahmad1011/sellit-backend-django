from rest_framework import serializers
from exduser.models import ExtendUser


class ExtendUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendUser
        fields = ['matrikel_number', 'dob', 'address',
                  'phone_number']


# ['id', 'matrikel_number', 'first_name', 'last_name', 'dob', 'email', 'address',
#                   'phone_number', 'username', 'password']