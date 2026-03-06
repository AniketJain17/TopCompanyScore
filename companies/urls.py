from django.urls import path

from .views import CalculateScoreView, TopCompaniesView, CompanyDetailView

urlpatterns = [
    path('companies/calculate/', CalculateScoreView.as_view()),
    path('companies/top/', TopCompaniesView.as_view()),
    path('companies/<int:pk>/', CompanyDetailView.as_view()),
]