from django.urls import path
from websiteapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('change_theme/<str:theme>/', views.change_theme, name='change_theme'),
    path('mentions/', views.mentions, name='mentions'),
]
