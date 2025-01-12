from django.urls import path

from .views import recipe_index, recipe_list
app_name = 'recipesapp'

urlpatterns = [
    path('', recipe_index, name='index'),
    path('list/', recipe_list, name='list'),

]