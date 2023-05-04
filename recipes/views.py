from django.db.models import Q
from django.shortcuts import render
from recipes.models import Recipe
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse_lazy

class RecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    fields = ['title', 'level', 'description']

class RecipeListView(ListView):
    model = Recipe
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list

class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['title', 'level', 'description']

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = '__all__'

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes')

def user_recipes(request):
    recipe_list = Recipe.objects.filter(author_id=request.user)
    return render(request, 'recipes/recipe_list.html', {'recipe_list': recipe_list})
