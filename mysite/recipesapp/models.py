from django.contrib.auth.models import User
from django.db import models

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


    @property
    def description_short(self):
        if len(self.description) < 25:
            return self.description
        else:
            return self.description[:25] + "..."

    def __str__(self):
        return self.title