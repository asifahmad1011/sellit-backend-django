from django.urls import path
from products import views


urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('products/new', views.ProductsListCreate.as_view()),
    path('productbyid/<int:pk>', views.ProductsDetail.as_view()),
    path('productbysellerid/<int:seller_id>/', views.ProductsBySeller.as_view()),
]
