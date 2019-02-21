from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class RecipeList(ListView):
    model = Recipe

class RecipeDetail(DetailView):
    def get_object(self):
        recipe_id = self.kwargs['recipe_id']
        return Recipe.objects.get(public_id=recipe_id)