from django.urls import path, include
from websiteapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', include('websiteapp.aboutapp.urls')),
    path('blog/', include('websiteapp.blogapp.urls')),
    path('contact/', include('websiteapp.contactapp.urls')),
    path('portfolio/', include('websiteapp.portfolioapp.urls')),
    path('change_theme/<str:theme>/', views.change_theme, name='change_theme'),
    path('change_lang/<str:language>/', views.change_lang, name='change_lang'),
    path('mentions/', views.mentions, name='mentions'),
]
