from django.urls import path
from studentarchives import views

urlpatterns = [
    path('students/', views.StudentList.as_view()),
    # path('studentrec/', views.StudentList.as_view())
    path('studentarchivebyid/<int:matrikel_number>/', views.StudentDetail.as_view())
]