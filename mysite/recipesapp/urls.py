from django.urls import path

from .views import RecipeIndexView,\
    RecipeListView, \
    RecipeDetailsView,\
    recipe_create
app_name = 'recipesapp'

urlpatterns = [
    path('', RecipeIndexView.as_view(), name='index'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<int:pk>/', RecipeDetailsView.as_view(), name='recipe_details'),
    path('recipe/create/', recipe_create, name='recipe_create'),

]