from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

def home(request):
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
    context_object_name ='posts'
    ordering = ['date_posted']

    # This is a class based view which displays the relevant posts for the particular user in chronloigcal order.
