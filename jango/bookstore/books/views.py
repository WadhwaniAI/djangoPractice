from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.views.generic import ListView, DetailView

#Create your views here.
class BookListView(ListView):
    context_obj_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(DetailView):
#     review = Review.objects.filter(book_id=id).order_by('-created_at')
    model = Book
    pass


# def index(request):
#     dbData = Book.objects.all()
#     context = {'books': dbData}
#     return render(request, 'books/index.html', context)

# def show(request, id):
#     singeBook = get_object_or_404(Book, pk=id)
#     review = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singeBook, 'reviews':review} 
#     return render(request, 'books/show.html', context) 



def review(request, id):
    body = request.POST['review']
    Review(body=body, book_id=id).save()
    return redirect('/book') 
    