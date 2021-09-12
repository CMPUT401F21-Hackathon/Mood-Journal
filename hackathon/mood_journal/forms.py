from django import forms
from .models import Mood, Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['name','bio']
        
class MoodForm(forms.ModelForm):
    status = forms.CharField(initial="Untitled Mood")
    class Meta:
        model = Mood
        fields = ['status', 'recommendation',]