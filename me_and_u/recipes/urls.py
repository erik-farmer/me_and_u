from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.RecipeList.as_view(), name='recipe_list'),
]
