from django.urls import path
from websiteapp.blogapp import views


urlpatterns = [
    path('', views.blog, name='blog'),
]