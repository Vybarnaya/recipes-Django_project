from django import forms
from django.contrib.auth.models import User
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "title", "description", "steps_of_cooking", "time_for_cooking", "author", "archived"

