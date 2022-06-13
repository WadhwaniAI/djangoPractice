from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review

# Create your views here.
def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)

def show(request, id):
    singeBook = get_object_or_404(Book, pk=id)
    context = {'books': singeBook} 
    return render(request, 'books/show.html', context) 

def review(request):
    body = request.POST['review']
    Review(body=body).save()
    return redirect('/book')
    