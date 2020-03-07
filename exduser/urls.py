from django.urls import path
from exduser import views


urlpatterns = [
    path('user/', views.ExtendUserList.as_view()),
    path('user/<int:pk>', views.ExtendUserDetail.as_view()),
]
