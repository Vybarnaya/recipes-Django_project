from django.urls import path

from .views import RecipeIndexView,\
    RecipeListView, \
    RecipeDetailsView,\
    RecipeCreateView,\
    RecipeUpdateView,\
    RecipeDeleteView

app_name = 'recipesapp'

urlpatterns = [
    path('', RecipeIndexView.as_view(), name='index'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('recipe/create/', RecipeCreateView.as_view(), name='recipe_create'),
    path('list/<int:pk>/', RecipeDetailsView.as_view(), name='recipe_details'),
    path('list/<int:pk>/update', RecipeUpdateView.as_view(), name='recipe_update'),
    path('list/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe_delete'),
]