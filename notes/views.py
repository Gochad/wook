from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from notes.models import Note
#from .forms import NoteForm
from django.urls import reverse_lazy
class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'textplace']
    # initial = {'date': '11/06/2020'}

class NoteUpdate(UpdateView):
    model = Note
    fields = '__all__'

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes')

def user_notes(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'note_list.html', {'notes': notes})
