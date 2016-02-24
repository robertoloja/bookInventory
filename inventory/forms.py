from django.forms import ModelForm
from .models import Location, Book

class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'comments', 'location']

class ModifyBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'location', 'comments', 'id']

class AddLocForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']
