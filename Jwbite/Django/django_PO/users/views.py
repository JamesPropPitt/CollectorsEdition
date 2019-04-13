from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserUpdateFormForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserUpdateFormForm()
    return render(request, 'users/register.html', {'form': form})
    # This was in a tutorial I was using but is probably not necessary in the final build on the PO since I assume all users will have premade accounts made

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html')

    # Creating a context is a dictionary of keys which in this case are u_form and p_form; userupdate and profileupdate.
