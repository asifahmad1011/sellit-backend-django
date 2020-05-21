from django.urls import path

from brands import views

urlpatterns = [
    path('brands/', views.BrandsList.as_view()),
    path('brandbyid/<int:pk>', views.BrandsDetail.as_view()),
]
