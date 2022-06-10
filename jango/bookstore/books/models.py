from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=256, null=True) 
    pageCount = models.IntegerField(null=True)
    thumbnail_url = models.CharField(max_length=256, null=True)
    short_desc = models.CharField(max_length=256, null=True)
    long_desc = models.TextField(null=True)