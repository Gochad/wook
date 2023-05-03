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

class UserFilterView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'user_filtering'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            return Note.objects.filter(author_id=self.user)
        return None

def user_notes(request):
    note_list = Note.objects.filter(author_id=request.user)
    return render(request, 'notes/note_list.html', {'note_list': note_list})

class SearchView(ListView):
    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            return Note.objects.filter(title__contains=query)
        return None