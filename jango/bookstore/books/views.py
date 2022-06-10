from http.client import HTTPResponse
from django.shortcuts import render
from books.models import Book

# Create your views here.
def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)

def show(request, id):
    context = {'books': {
        'id':1,
        'title':'Definite Guide to Django',
        'thumbnail_url':'https://static.packt-cdn.com/products/9781838981952/cover/smaller'
    }} 
    return render(request, 'books/show.html', context)