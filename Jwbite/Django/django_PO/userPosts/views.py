from django.shortcuts import render
from .models import Post
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from django import template



def home(request):
    if user.is_authenticated:
        context = {
            'posts':Post.objects.filter(author=request.user)
        }
    if user.is_superuser:
        context = {
            'posts': Post.objects.all()
        }
        return render(request, 'userPosts/previousSprints.html', context)
    # This is what the program executes to populate the previousSprints page

def about(request):
    return render(request, 'userPosts/about.html', {'title': 'About'})
    #  This is what the program executes to populate the about page, can probably be removed at some point.

def user(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    # This function gets whether the user is logged in and, if true, returns the user's username.

@login_required
def profile(request):
    return render(request, 'userPosts/profile.html')
    # This function requires the user to be logged in and if they are, populates the profile page for the user.

class PostListView(ListView):
    model = Post
    template_name = 'userPosts/previousSprints.html'
    context_object_name = 'posts'
    paginate_by = 5

    # This is a class based view which displays the relevant posts for the particular user in chronological order.

class UserPostListView(ListView):
    model = Post
    template_name = 'userPosts/previousSprints.html'
    context_object_name ='posts'
    paginate_by = 20

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    # Paginates the posts on the page to display 1 per page (1 per sprint)

class PostDetailView(DetailView):
    model = Post
    # View post alone

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    User = get_user_model()

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    # Only the author of the post will be allowed to make changes to the post (with the exception of the admin, who will be able to do everything anyway)
    # This is required for updating a post, but given the nature of the Product Owner application, it might not be appropriate for users to be able to modify previous posts.

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # Write the current logged in user as the author, as such 'LoginRequiredMixin' is an import which requires the user to be logged in and makes them login otherwise

register = template.Library()
@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()



