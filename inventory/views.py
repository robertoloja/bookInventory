from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator

from .models import Book, Location
from .forms import AddBookForm, ModifyBookForm, AddLocForm


@method_decorator(xframe_options_exempt):
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


def deleteLocation(request):
    for location in request.POST.getlist('selectedLocations'):
        Location.objects.get(id=location).delete()
    return HttpResponseRedirect("/modLocations/")


def modifyLocations(request):
    locations = Location.objects.all()

    if request.method == 'POST':
        form = AddLocForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("inventory/modLoc.html")

    else:
        form = AddLocForm()

    return render(request, 'inventory/modLoc.html', {
        'locations': locations,
        'form': form,
        })

def search(request):
    query = request.GET['q'].split(' ')
    query = map(lambda x: x.lower(), query)

    objects = Book.objects.all()

    def matches(thing):
        fields = []
        for i in thing.author.lower().split(' '):
            fields.append(i)

        for i in thing.title.lower().split(' '):
            fields.append(i)

        for i in thing.location.name.lower().split(' '):
            fields.append(i)

        for i in thing.comments.lower().split(' '):
            fields.append(i)

        for word in query:
            if word in fields:
                return True

    objects = filter(matches, objects)

    return render(request, 'inventory/results.html', {
        'books': objects,
        })
