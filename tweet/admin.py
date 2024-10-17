from django.contrib import admin
from .models import Recipe, Tweet



# Register your models here.

admin.site.register(Tweet)
admin.site.register(Recipe)