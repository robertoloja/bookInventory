from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Book, Location
from .forms import AddBookForm

def index(request):
    books = Book.objects.all()
    locations = Location.objects.all()

    if request.method == 'POST':
        form = AddBookForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = AddBookForm()

    return render(request, 'inventory/index.html', {
        'books': books,
        'locations': locations,
        'form': form,
        })
