from django.urls import path

from .views import recipe_index, recipe_list, recipe_create
app_name = 'recipesapp'

urlpatterns = [
    path('', recipe_index, name='index'),
    path('list/', recipe_list, name='list'),
    path('recipe/create/', recipe_create, name='recipe_create'),

]