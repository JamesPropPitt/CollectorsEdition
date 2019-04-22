from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = {'username', 'email'}
# Allows the user to update their username and email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
# Allows the user to update their image

class GameChoice(forms.Form):
    gameid = forms.CharField(required=True, max_length=50, widget=forms.HiddenInput())
    studentid = forms.CharField(required=True, max_length=50, widget=forms.HiddenInput())
    votecodeid = forms.CharField(required=True, max_length=50, widget=forms.HiddenInput())
    def clean(self):
        student = Student.objects.filter(id=self.cleaned_data['studentid']).first()
        votecode = VoteCode.objects.filter(id=self.cleaned_data['gameid']).first()