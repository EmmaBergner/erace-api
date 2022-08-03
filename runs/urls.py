from django.urls import path
from runs import views 

urlpatterns = [
    path('runs/', views.RunList.as_view()),
    path('runs/<int:pk>/', views.RunDetail.as_view()),
]