from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from userPosts import views as user_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='userPosts-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #pk = primary key ( the number of the post). pk is the naming convention of postdetail
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # As explained in views.py it might not be appropriate for this to be in the final build
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='userPosts-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]

# This is a very important .py file that works as a signpost for the website. When it receives an alert, it will point the website in the correct direction with the varying rulesets given.
# SO if the website were redirecting to the login page, the login page would display login.html and auth_views.LoginView.as_view which is Django's built in login functionality.

