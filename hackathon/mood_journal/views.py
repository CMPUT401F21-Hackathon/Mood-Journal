from django.shortcuts import redirect, render
from .forms import MoodForm
from .recomendations import music

# Create your views here.

def home(request):
    return render(request, 'mood_journal/home.html')

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

   