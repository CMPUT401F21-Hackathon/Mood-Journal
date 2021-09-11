from django.shortcuts import redirect, render
from .forms import MoodForm

# Create your views here.

def home(request):
    return render(request, 'mood_journal/home.html')

def mood_new(request):
    if request.method == "POST":
        form = MoodForm(request.POST)
        if form.is_valid:
            mood = form.save(commit=False)
            mood.user = request.user.profile
            mood.save()
            return redirect("mood_journal:home")
    else:
        form = MoodForm()
    return render(request, 'mood_journal/mood_edit.html', {'form': form})

   