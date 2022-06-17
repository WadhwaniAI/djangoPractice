from cgi import FieldStorage
from django.shortcuts import redirect, render
from books.models import Book, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage

#Create your views here.
# def index(request):
#     login_url = '/login/'
#     dbData = Book.objects.all()
#     context = {'books': dbData}  
#     return render(request, 'books/book_list.html', context)

class BookListView(LoginRequiredMixin, ListView):
    login_url = '/login/'

    def get_queryset(self):
         return Book.objects.all()
    
    
class BookDetailView(DetailView, LoginRequiredMixin):
#   review = Review.objects.filter(book_id=id).order_by('-created_at')
    login_url = '/login/'
    model = Book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].author.all()
        return context
 
# def show(request, id): 
#     singeBook = get_object_or_404(Book, pk=id)
#     review = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singeBook, 'reviews':review} 
#     return render(request, 'books/show.html', context) 
 


def review(request, id):
    image = request.FILES['image']
    fs = FileSystemStorage()
    name = fs.save(image.name, image)
    body = request.POST['review']
    newReview = Review(body=body, book_id=id, image=fs.url(name))
    newReview.save()
    return redirect('/book') 

def author(request, author):
    books = Book.objects.filter(author__name=author)
    context = {'books': books}
    return render(request, 'books/book_list.html', context)

