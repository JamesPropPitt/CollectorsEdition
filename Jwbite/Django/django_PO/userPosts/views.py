from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'userPosts/home.html', context)

def about(request):
    return render(request, 'userPosts/about.html', {'title': 'About'})

def user(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

@login_required
def profile(request):
    return render(request, 'userPosts/profile.html')