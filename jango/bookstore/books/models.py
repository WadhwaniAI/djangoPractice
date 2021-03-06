from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=256, null=True) 
    pageCount = models.IntegerField(null=True)
    short_desc = models.CharField(max_length=256, null=True)
    long_desc = models.TextField(null=True)
    author = models.ManyToManyField(Author)
    image = models.ImageField(upload_to='images', null=True)
    
    def __str__(self):
        return f"{self.id} {self.title}"
    
class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/reviews', null=True)
    
    def __str__(self):
        return self.body
    