from django.forms import ModelForm
from django import forms
from .models import Joke

class JokeForm(ModelForm):
    joke_text = forms.TextInput()
    punchline = forms.TextInput()
    age = forms.TextInput()

    class Meta:
        model = Joke
        fields = ["joke_text", "punchline", "age_appropriate"]