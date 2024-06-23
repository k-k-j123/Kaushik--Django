# models.py

from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    procedure = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url=models.CharField(default='imageurl',max_length=500)

    def __str__(self):
        return self.name

class DefaultRecipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    procedure = models.TextField()
    image_url=models.CharField(default='imageurl',max_length=500)

    def __str__(self):
        return self.name