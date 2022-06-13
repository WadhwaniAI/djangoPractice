from django.shortcuts import redirect, render
from books.models import Book, Review
from django.views.generic import ListView, DetailView

#Create your views here.
def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}  
    return render(request, 'books/book_list.html', context)

class BookDetailView(DetailView):
#     review = Review.objects.filter(book_id=id).order_by('-created_at')
    model = Book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].author.all()
        return context
        
    pass




# def show(request, id): 
#     singeBook = get_object_or_404(Book, pk=id)
#     review = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singeBook, 'reviews':review} 
#     return render(request, 'books/show.html', context) 



def review(request, id):
    body = request.POST['review']
    Review(body=body, book_id=id).save()
    return redirect('/book') 

def author(request, author):
    books = Book.objects.filter(author__name=author)
    context = {'books': books}
    return render(request, 'books/book_list.html', context)
