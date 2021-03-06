from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User

import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=100, blank=True)
    bio = models.TextField(max_length=200, blank=True)

class Mood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=200, blank=True, help_text="Tell me how you are feeling!")
    timestamp = models.DateTimeField(default=timezone.now)
    # 0-49: Sad; 50: Neutral; 51-100: Happy
    score = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    class RecommendationChoices(models.TextChoices):
        MOVIE = 'Movie',
        MUSIC = 'Music',
        FOOD = 'Food'

    recommendation = models.TextField(
        max_length=40,
        choices=RecommendationChoices.choices,
        default=RecommendationChoices.MUSIC
    )

    link_title = models.TextField(max_length=200, blank=True)
    link = models.TextField(max_length=200, blank=True)

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)