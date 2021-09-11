from .models import Mood
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MoodForm
from .models import Mood, Profile
from .recomendations import music
import json

# Create your views here.

def home(request):
    current_profile = request.user.profile
    moods = Mood.objects.filter(user=current_profile).order_by('-timestamp')
    moods_r = Mood.objects.filter(user=current_profile).order_by('timestamp')
    labels = []
    data = []
    for mood in moods_r:
        labels.append(mood.timestamp.strftime("%m/%d/%Y, %H:%M:%S"))
        data.append(mood.score)
    context = {
        'moods': moods,
        'labels': labels,
        'data': data,
    }
    return render(request, 'mood_journal/home.html', context)

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
            mood.score = request.POST.get('range')
            mood.save()
            return redirect("mood_journal:home")
    else:
        form = MoodForm(instance=mood)
        score_slider = mood.score

    return render(request,'mood_journal/mood_edit.html', {'form': form, 'score_slider': score_slider})

   