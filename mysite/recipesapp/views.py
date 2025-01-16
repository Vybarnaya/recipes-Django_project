from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .forms import RecipeForm
from .models import Recipe

class RecipeIndexView(View):
    def get(self, request: HttpRequest):
        return render(request, "recipesapp/recipe-index.html")

# def recipe_index(request: HttpRequest):
#     return render(request, "recipesapp/recipe-index.html")
#     # recipes = models.Recipe.objects.all()
#     # context = {'recipes': recipes}
#     # return render(request, 'recipesapp/recipe-index.html', context)

class RecipeListView(ListView):
    template_name ='recipesapp/recipes-list.html'
    model = Recipe
    context_object_name = "recipes"


# class RecipeListView(View):
#     def get(self, request: HttpRequest):
#         recipes = Recipe.objects.all()
#         context = {'recipes': recipes}
#         return render(request, "recipesapp/recipes-list.html", context=context)
#     def post(self):
#         pass

class RecipeDetailsView(DetailView):
    template_name = "recipesapp/recipe-details.html"
    model = Recipe
    context_object_name = "recipe"

    # def get(self, request: HttpRequest, pk: int):
    #     recipe = get_object_or_404(Recipe, pk=pk)
    #     context = {'recipe': recipe}
    #     return render(request, , context=context)



# def recipe_list(request: HttpRequest):
#     recipes = Recipe.objects.all()
#     context = {'recipes': recipes}
#     return render(request, "recipesapp/recipes-list.html", context=context)

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


