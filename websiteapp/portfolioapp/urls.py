from django.urls import path
from websiteapp.portfolioapp import views


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<str:project_name>/', views.project),
]
