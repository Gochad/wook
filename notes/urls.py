from django.urls import path
from .views import NoteListView, NoteDetailView, NoteCreate, user_notes

urlpatterns = [
    path("", NoteListView.as_view(), name='note_list'),
    path("user/", user_notes, name='user_notes'),
    path("<int:pk>/", NoteDetailView.as_view(), name='note_detail'),
    path("add_new/", NoteCreate.as_view(), name='add_new'),
]