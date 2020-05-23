from django.urls import path

from chat import views

urlpatterns = [
    path('chat/', views.ChatList.as_view()),
    path('chatbyuser/<int:pk>', views.ChatDetail.as_view()),

]
