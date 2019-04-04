from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from userPosts import views as user_views

urlpatterns = [
    path('', views.home, name='userPosts-home'),
    path('login/', auth_views.LoginView.as_view(template_name='userPosts/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='userPosts/logout.html'), name='logout'),
    path('about/', views.about, name='userPosts-about'),
    path('profile/', user_views.profile, name='profile'),
]

