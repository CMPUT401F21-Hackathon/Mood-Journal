from django import forms
from .models import Mood

class MoodForm(forms.ModelForm):
    status = forms.CharField(initial="Untitled Mood")
    class Meta:
        model = Mood
        fields = ['status', 'recommendation',]