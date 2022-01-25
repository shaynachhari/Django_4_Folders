from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='indexhtml'),
    path('contact/', views.contact, name='contacthtml'),
    path('about/', views.about, name='abouthtml'),
    path('login/', views.login, name='loginhtml')
]
