from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from recipesapp.models import Recipe
@admin.action(description="Archive recipe")
def mark_arhived_recipe(modeladmin:admin.ModelAdmin, request:HttpRequest, queryset:QuerySet):
    queryset.update(archived=True)

@admin.action(description="Unarchive recipe")
def mark_unarhived_recipe(modeladmin:admin.ModelAdmin, request:HttpRequest, queryset:QuerySet):
    queryset.update(archived=False)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    actions = [mark_arhived_recipe, mark_unarhived_recipe]
    list_display = 'id', 'title', 'description', "created_at", "updated_at", "archived"
    list_display_links = 'id', 'title'
    search_fields = ['title', 'description']

class AuthorAdmin(admin.ModelAdmin):
    list_display = 'id', 'username', 'email', "created_at", "updated_at"