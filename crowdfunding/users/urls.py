from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomerUserDetail.as_view()),
    path('user/stats/', views.UserStats.as_view()),
    path('user/profile/', views.UserProfile.as_view()),
    ]