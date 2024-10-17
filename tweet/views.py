from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

# Create your views here.


def base(request):
    return render(request, 'base.html')

def index(request):
    recipes = Recipe.objects.all()
    print("Available Recipe IDs:", [recipe.id for recipe in recipes])
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )
        return redirect('/tweet/index/')

    queryset = Recipe.objects.all()
    context = {'recipe': queryset}


    return render(request, 'index.html',context)


def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('/tweet/index/')


