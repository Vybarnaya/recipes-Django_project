from django.contrib import admin

from recipesapp.models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', "created_at", "updated_at"
    list_display_links = 'id', 'title'
    search_fields = ['title', 'description']