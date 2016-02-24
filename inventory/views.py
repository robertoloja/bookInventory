from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView

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
    print(request.POST.get('deleteModify'))
    if request.POST.get('deleteModify') == 'delete':
        return deleteBook(request)

    elif request.POST.get('deleteModify') == 'modify':
        url = '/savemod/' + request.POST.getlist('selectedBooks')[0] + '/'
        return HttpResponseRedirect(url)

    else:
        return HttpResponseRedirect("/")

class UpdateBook(UpdateView):
    model = Book
    form_class = ModifyBookForm
    template_name = 'inventory/modify.html'
    success_url = '/'


def deleteBook(request):
    for bookId in request.POST.getlist('selectedBooks'):
        Book.objects.get(id=bookId).delete()
    return HttpResponseRedirect("/")
