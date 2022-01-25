from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contactus', views.contact, name='contact'),
    path('login/', views.login, name='login')

]
