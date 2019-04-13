from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from userPosts import views as user_views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='userPosts-home'),
    path('about/', views.about, name='userPosts-about'),
]

# This is a very important .py file that works as a signpost for the website. When it receives an alert, it will point the website in the correct direction with the varying rulesets given.
# SO if the website were redirecting to the login page, the login page would display login.html and auth_views.LoginView.as_view which is Django's built in login functionality.

