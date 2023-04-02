from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Widget (models.Model):
    name = models.CharField(max_length=10)

class Joke (models.Model):
    user = models.ForeignKey(
        User,
        related_name="Jokes",
        on_delete=models.CASCADE
    )
    joke_text = models.TextField()
    punchline = models.CharField(max_length=255, null=True)
    is_funny = models.BooleanField(default=False)
    flag_offensive = models.BooleanField(default=False)
    age_appropriate = models.IntegerField(default=5)
