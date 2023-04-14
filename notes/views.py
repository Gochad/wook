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

class NoteUpdate(UpdateView):
    model = Note
    fields = '__all__'

class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('notes')

def user_notes(request):
    note_list = Note.objects.filter(author_id=request.user)
    return render(request, 'user_notes.html', {'note_list': note_list})
