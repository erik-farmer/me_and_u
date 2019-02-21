from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:recipe_id>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
