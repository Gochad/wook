from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreate

urlpatterns = [
    path("", NoteListView.as_view(), name='note_list'),
    path("<int:pk>/", NoteDetailView.as_view(), name='note_detail'),
    path("add_new/", NoteCreate.as_view(), name='add_new'),
]