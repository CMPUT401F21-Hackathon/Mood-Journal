from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserChangeForm
from mood_journal.models import Profile
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'mood_journal/home.html')

def edit_profile(request):
    return render(request, 'registration/edit_profile.html')

