from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Users


class UsersSerializer(serializers.ModelSerializer):
    # users = UserSerializer()

    class Meta:
        model = Users
        fields = ['matrikel_number', 'dob', 'address', 'phone_number', 'postal_code']


class UserSerializer(serializers.ModelSerializer):
    # users = serializers.PrimaryKeyRelatedField(many=True, queryset=Users.objects.all())
    # password = serializers.CharField(max_length=255,
    # style={'input_type': 'password'})
    users = UsersSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'users']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
