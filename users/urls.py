from django.urls import path
from users import views


urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('register/', views.UsersList.as_view()),
    path('userbyid/<int:pk>', views.UsersDetail.as_view()),

]