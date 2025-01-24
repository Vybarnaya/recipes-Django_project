from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
import logging

from userslist.models import Profile
from .forms import RecipeForm
from .models import Recipe




log = logging.getLogger(__name__)
class RecipeIndexView(View):
    def get(self, request: HttpRequest):
        log.info("User accessed recipe index page")

        return render(request, "recipesapp/recipe-index.html")

class RecipeListView(ListView):
    template_name ='recipesapp/recipes-list.html'
    # model = Recipe
    context_object_name = "recipes"
    queryset = Recipe.objects.filter(archived=False)


class RecipeDetailsView(DetailView):
    template_name = "recipesapp/recipe-details.html"
    model = Recipe
    context_object_name = "recipe"

class RecipeCreateView(CreateView):
    model = Recipe
    # form_class = RecipeForm
    fields = "title", "description", "steps_of_cooking", "time_for_cooking", "author", "photo"
    success_url = reverse_lazy('recipesapp:list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class RecipeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'recipesapp.change_recipe'
    model = Recipe
    fields = "title", "description", "time_for_cooking", "steps_of_cooking", "photo"
    template_name_suffix = "_update_form"
    def get_success_url(self):
        return reverse('recipesapp:recipe_details',
                       kwargs={"pk":self.object.pk},)

class RecipeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'recipesapp.delete_recipe'
    model = Recipe
    success_url = reverse_lazy('recipesapp:list')
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)





