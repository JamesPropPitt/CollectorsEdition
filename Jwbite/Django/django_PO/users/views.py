from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.template.response import TemplateResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

def register(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserUpdateForm()
    return render(request, 'users/register.html', {'form': form})
    # This was in a tutorial I was using but is probably not necessary in the final build on the PO since I assume all users will have premade accounts made

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.isvalid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        # This requests a post and, if the information that the user has filled in is applicable and appropriate, updates the user's profile. Could also maybe delete this in the final build.

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

    # Creating a context is a dictionary of keys which in this case are u_form and p_form; userupdate and profileupdate.

@login_required
def index(request):
    group = request.user.groups.order_by('name').first()
    if group:
        return redirect('groups_show',group.name)
    else:
        return TemplateResponse(request,'userPosts/logout.html')
