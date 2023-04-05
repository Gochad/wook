from datetime import timezone

from django.shortcuts import render
from recipes.models import Recipe, IngredientInRecipe
from django.views.generic import ListView, DetailView
from django import forms

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    fields = ['title', 'level', 'description']

class RecipeListView(ListView):
    model = Recipe


class RecipeDetailView(DetailView):
    model = Recipe
    # form_class = RecipeForm
    context_object_name = 'recipe'

