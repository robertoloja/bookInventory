from django.forms import ModelForm
from .models import Location, Book

class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'read', 'location']

class ModifyBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'location']
