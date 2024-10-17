from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.base, name="base"),
    path('index/', views.index, name= "home"),
    path('delete_recipe/<int:id>/', views.delete_recipe, name= "delete_recipe"),
]
