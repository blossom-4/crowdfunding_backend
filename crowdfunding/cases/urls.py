from django.urls import path
from . import views

urlpatterns = [
    path('cases/', views.CaseList.as_view()),
    path('cases/<int:pk>/', views.CaseDetail.as_view()),
    path('judgements/', views.JudgementList.as_view()),
    path('judgements/<int:pk>/', views.JudgementDetail.as_view()),
    ]