from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.TextField(null=False, max_length=200)
    image = models.ImageField(upload_to= 'images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    



class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to= "images")

    def __str__(self):
        return self.recipe_name