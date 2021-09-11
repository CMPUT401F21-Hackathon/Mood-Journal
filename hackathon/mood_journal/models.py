from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=100, blank=True)
    bio = models.TextField(max_length=100, blank=True)

class Mood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(default=timezone.now)
    # 0-49: Sad; 50: Neutral; 51-100: Happy
    score = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
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

    user = models.ForeignKey(User, on_delete=models.CASCADE)