from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

class RecipeList(ListView):
    def get_queryset(self):
        return Recipe.objects.all().values('public_id', 'name')

class RecipeDetail(DetailView):
    template_name = 'recipes/recipe_detail.html'

    def get_context_object_name(self, obj):
        return 'recipe'

    def get_object(self):
        recipe_id = self.kwargs['recipe_id']
        return Recipe.objects.values(
            'name',
            'url',
            'ingredients',
            'steps',
            'notes',
        ).get(public_id=recipe_id)
