from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Recipe

def recipe_index(request: HttpRequest):
    return render(request, "recipesapp/recipe-index.html")
    # recipes = models.Recipe.objects.all()
    # context = {'recipes': recipes}
    # return render(request, 'recipesapp/recipe-index.html', context)

def recipe_list(request: HttpRequest):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, "recipesapp/recipes-list.html", context=context)



