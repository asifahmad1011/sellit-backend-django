from django.urls import path
from category import views

urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/add/', views.CategoryCreate.as_view()),
    path('categorybyid/<int:pk>', views.CategoryDetail.as_view()),
]
