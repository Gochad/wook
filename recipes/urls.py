from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreate

urlpatterns = [
    path("", RecipeListView.as_view(), name='recipe_list'),
    path("<int:pk>/", RecipeDetailView.as_view(), name='recipe_detail'),
    path("add_new/", RecipeCreate.as_view(), name='add_new'),
]