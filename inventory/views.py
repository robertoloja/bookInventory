from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Book, Location
from .forms import AddBookForm, ModifyBookForm

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
    if request.POST.get('deleteModify') == 'delete':
        return deleteBook(request)

    elif request.POST.get('deleteModify') == 'modify':
        book = Book.objects.get(id=request.POST.getlist('selectedBooks')[0])
        print(book)
        form = ModifyBookForm(instance=book)

        return render(request, 'inventory/modify.html', {
            'book': book,
            'form': form,
            })
    else:
        form = ModifyBookForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")


def deleteBook(request):
    for bookId in request.POST.getlist('selectedBooks'):
        Book.objects.get(id=bookId).delete()
    return HttpResponseRedirect("/")
