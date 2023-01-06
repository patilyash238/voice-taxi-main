from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signupform, name="signupform"),
    path('signin', views.signinform, name="signinform"),
    path('logout', views.logoutview, name="logout"),
    path('firenotification', views.noti, name="notification"),
    path('booktaxi', views.bookataxi, name="booktaxi"),
]
