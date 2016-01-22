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

def modifyBook(request):
    print(request.POST.getlist('selectedBooks'))
    if request.POST.get('deleteModify') == 'delete':
        return deleteBook(request)
    else:
        return render(request, 'inventory/modify.html')

def deleteBook(request):
    for bookId in request.POST.getlist('selectedBooks'):
        Book.objects.get(id=bookId).delete()
    return HttpResponseRedirect("/")
