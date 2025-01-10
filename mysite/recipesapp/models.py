from django.db import models

from django.db import models

class Recipe(models.Model):

    class Meta:
        verbose_name = "Recipe"

    title = models.CharField(max_length=150)
    description = models.TextField()
    steps_of_cooking = models.TextField()
    time_for_cooking = models.IntegerField(default=15)

    def __str__(self):
        return self.title