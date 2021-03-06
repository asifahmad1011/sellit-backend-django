from django.urls import path, re_path
from products import views

urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('products/new', views.ProductsListCreate.as_view()),
    path('productbyid/<int:pk>', views.ProductsDetail.as_view()),
    path('updateproduct/<int:pk>', views.ProductsDetail.as_view()),
    path('deleteproduct/<int:pk>', views.ProductsDetail.as_view()),
    path('productbysellerid/<int:seller_id>/', views.ProductsBySeller.as_view()),
    path('productbyname/', views.ProductsByName.as_view()),
]
