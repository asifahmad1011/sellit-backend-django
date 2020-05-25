from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    email = EmailField(label='Email')
    password2 = CharField(label='Confirm Password', style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'username', 'email', 'password', 'password2'
        )
        extra_kwargs = {"password": {"write_only": True, "style": {'input_type': 'password'}}
                        }

    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('password2')
        if password1 != password2:
            raise ValidationError('Password Not Matched!')
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError('This user is already registered!')
        return data

    def create(self, validated_data):
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['password2']
        user_obj = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user_obj.set_password(password and password2)
        user_obj.save()
        return validated_data
