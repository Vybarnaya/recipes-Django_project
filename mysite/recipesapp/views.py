from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse

from .forms import RecipeForm
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

def recipe_create(request: HttpRequest):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Recipe.objects.create(**form.cleaned_data)
            form.save()

            url = reverse('recipesapp:list')
            return redirect(url)
    else:
        form = RecipeForm()

    context = {'form': form}
    return render(request, "recipesapp/create-recipe.html", context=context)


