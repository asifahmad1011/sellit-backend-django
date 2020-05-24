from rest_framework import serializers
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields=['product', 'sender', 'receiver', 'message', 'created_date']