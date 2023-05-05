from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from notes.models import Note
class NoteListView(ListView):
    model = Note
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Note.objects.filter(
            Q(title__icontains=query) | Q(textplace__icontains=query)
        )
        return object_list

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
    return render(request, 'notes/note_list.html', {'note_list': note_list})
