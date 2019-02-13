from django.urls import path
from websiteapp.aboutapp import views


urlpatterns = [
    path('', views.about, name='about'),
]
