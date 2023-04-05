from django.shortcuts import render
from django.views.generic import ListView, DetailView
from notes.models import Note

class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note
    # form_class = RecipeForm
    context_object_name = 'note'
