from django.contrib.auth.models import User
from django.db import models

def recipe_photo_directory_path(instance:"Recipe", filename: str):
    return "recipies/recipe_{pk}/photo/{filename}".format(
        pk=instance.pk,
        filename=filename,)


class Recipe(models.Model):
    class Meta:
        verbose_name = "Recipe"
        # ordering = ['-created_at']  # Sort by most recently created first
        ordering = ['-title', 'created_at']

    title = models.CharField(max_length=150)
    description = models.TextField()
    steps_of_cooking = models.TextField()
    time_for_cooking = models.IntegerField(default=15)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    photo = models.ImageField(null=True,  blank=True, upload_to=recipe_photo_directory_path)

    @property
    def description_short(self):
        if len(self.description) < 25:
            return self.description
        else:
            return self.description[:25] + "..."

    def __str__(self):
        return self.title



