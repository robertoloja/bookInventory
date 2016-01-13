from django.forms import ModelForm
from .models import Location, Book

class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'location']
