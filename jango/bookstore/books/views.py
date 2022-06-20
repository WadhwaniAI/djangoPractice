from cgi import FieldStorage
from django.shortcuts import redirect, render
from books.models import Book
from books.form import ReviewForm
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
    model = Book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].author.all()
        context['form'] = ReviewForm
        return context
 
# def show(request, id): 
#     singeBook = get_object_or_404(Book, pk=id)
#     review = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book': singeBook, 'reviews':review} 
#     return render(request, 'books/show.html', context) 
 


def review(request, id):
    
    form = ReviewForm(request.POST)
    
    if form.is_valid():
        form.save()
    else:
        print('form invalid')
    
    # body = request.POST['body']
    # newReview = Review(body=body, book_id=id, user=request.user)
    
    # if len(request.FILES) != 0:
    #     image = request.FILES['image']
    #     fs = FileSystemStorage()
    #     name = fs.save(image.name, image)
    #     newReview.image = fs.url(name)
    # newReview.save()
    
    return redirect(f'/book/{id}') 

def author(request, author):
    books = Book.objects.filter(author__name=author)
    context = {'books': books}
    return render(request, 'books/book_list.html', context)

