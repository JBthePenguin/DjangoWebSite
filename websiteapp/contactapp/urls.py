from django.urls import path
from websiteapp.contactapp import views


urlpatterns = [
    path('', views.contact, name='contact'),
]
