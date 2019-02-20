from django.views.generic.list import ListView
from .models import Recipe

class RecipeList(ListView):
    model = Recipe
