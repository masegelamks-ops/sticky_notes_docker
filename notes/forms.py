# forms.py
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'color']  # Include the color field
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':
                                            'Title', 'class':
                                            'note-title-input'}),
            'content': forms.Textarea(attrs={'placeholder': 'Take a note...',
                                             'rows': 4, 'class':
                                             'note-content-input'}),
            'color': forms.TextInput(attrs={'type': 'color'})}
