from django.shortcuts import render

# Create your views here.
from chat.serializers import ChatSerializer
from rest_framework import generics

from chat.models import Chat


class ChatList(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
