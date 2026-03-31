from django.contrib import admin
from django.urls import path
from . import views
app_name = 'newApp'
urlpatterns = [
    path('', views.app,name='app'),
    path('about/', views.about,name='about'),
    
]