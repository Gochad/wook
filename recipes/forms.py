from django import forms

class RecipeSearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control me-2',
                'type': 'search',
                'placeholder': 'Search',
                'aria-label': 'Search',
            }
        )
    )