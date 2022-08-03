from django.urls import path
from races import views 

urlpatterns = [
    path('races/', views.RaceList.as_view()),
    path('races/<int:pk>/', views.RaceDetail.as_view()),
]