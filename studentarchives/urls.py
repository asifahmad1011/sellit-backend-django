from django.urls import path
from studentarchives import views

urlpatterns = [
    path('studentsrecords/', views.StudentList.as_view()),
    # path('studentrec/', views.StudentList.as_view())
    path('studentsrecordbyid/<int:matrikel_number>/', views.StudentDetail.as_view())
]