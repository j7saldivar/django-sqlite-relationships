from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=30)
    
class Book(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    