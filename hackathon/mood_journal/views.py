from django.shortcuts import render
from .models import Mood
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MoodForm
from .recomendations import music
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'mood_journal/home.html')

'''
def edit_profile(request):  
    return render(request, 'registration/edit_profile.html')
'''

from .forms import ProfileUpdateForm
def edit_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('mood_journal:home')
    else:
        p_form = ProfileUpdateForm(instance=request.user)

    context={'p_form': p_form}

    return render(request, 'registration/edit_profile.html',context)

def mood_new(request):
    if request.method == "POST":
        form = MoodForm(request.POST)
        if form.is_valid:
            mood = form.save(commit=False)
            mood.score = request.POST.get('range')
            mood.link = music["Never Gonna Give You Up"]
            mood.user = request.user.profile
            mood.save()
            return redirect("mood_journal:home")
    else:
        form = MoodForm()
    return render(request, 'mood_journal/mood_edit.html', {'form': form})

def mood_edit(request, pk):
    mood = get_object_or_404(Mood, pk=pk)
    if request.method =="POST":
        form = MoodForm(request.POST, instance=mood)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.save()
            return redirect("mood_journal:home")
    else:
        form = MoodForm(instance=mood)

    return render(request,'mood_journal/mood_edit.html', {'form': form})

   
