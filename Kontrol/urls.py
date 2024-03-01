from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('exit',views.exit,name='exit'),
    path('ayaz',views.ayaz,name='ayaz'),
]