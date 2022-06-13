from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=256, null=True) 
    pageCount = models.IntegerField(null=True)
    thumbnail_url = models.CharField(max_length=256, null=True)
    short_desc = models.CharField(max_length=256, null=True)
    long_desc = models.TextField(null=True)
    author = models.ManyToManyField(Author)
    
    def __str__(self):
        return f"{self.id} {self.title}"
    
class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.body
    