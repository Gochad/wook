from .models import Note
from django import forms

class NoteSearchForm(forms.Form):
    search_text =  forms.CharField(
    required = False,
    label='Search title',
    widget=forms.TextInput(attrs={'placeholder': 'Search'})
)