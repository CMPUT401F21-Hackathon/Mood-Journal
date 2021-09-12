from django.shortcuts import render
from .models import Mood
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MoodForm, ProfileUpdateForm
from .recomendations import music, movie, recipe, music_video
from django.contrib import messages
import json
import random


# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    current_profile = request.user.profile
    moods = Mood.objects.filter(user=current_profile).order_by('-timestamp')
    moods_r = Mood.objects.filter(user=current_profile).order_by('timestamp')
    labels = []
    data = []
    last_music = Mood.objects.filter(user=current_profile, recommendation='Music').order_by('-timestamp')[0]
    video = music_video.get(str(last_music.link_title))
    for mood in moods_r:
        labels.append(mood.timestamp.strftime("%m/%d, %H:%M"))
        data.append(mood.score)
    context = {
        'video': video,
        'moods': moods,
        'labels': labels,
        'data': data,
    }
    return render(request, 'mood_journal/home.html', context)

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    current_profile = request.user.profile
    context = {"profile": current_profile}

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
        if p_form.is_valid():
            p_form.save()
            current_profile.name = request.POST.get("name")
            current_profile.bio = request.POST.get("bio")
            current_profile.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('mood_journal:home')
            '''        
        else:
            p_form = ProfileUpdateForm(
                initial = {
                    "name": current_profile.name,
                    "bio": current_profile.bio
                }
            )
    
        context['p_form'] = p_form

    else:
        p_form = ProfileUpdateForm(
            initial = {
                "name": current_profile.name,
                "bio": current_profile.bio
            }
        )
    
    context['p_form'] = p_form
    print(p_form.fields["name"])
'''
    return render(request, 'registration/edit_profile.html',context)

def mood_new(request):
    if request.method == "POST":
        form = MoodForm(request.POST)
        if form.is_valid:
            mood = form.save(commit=False)
            mood.score = request.POST.get('range')
            if mood.recommendation == "Music":
                mood.link_title, mood.link = random.choice(list(music.items()))
            elif mood.recommendation == "Movie":
                mood.link_title, mood.link = random.choice(list(movie.items()))
            else: 
                mood.link_title, mood.link = random.choice(list(recipe.items()))
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
            mood.score = request.POST.get('range')
            mood.save()
            return redirect("mood_journal:home")
    else:
        form = MoodForm(instance=mood)
        score_slider = mood.score

    return render(request,'mood_journal/mood_edit.html', {'form': form, 'score_slider': score_slider})

   
