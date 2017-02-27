from django.db import models
from concurrency.fields import IntegerVersionField
from django.core.urlresolvers import resolve

class Author(models.Model):
    author_name = models.CharField(max_length=30)
    
class Category(models.Model):
    category = models.CharField(max_length=30)

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, db_table='bookapp_category_book')
    
class Stock(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, primary_key=True)
    quantity = models.IntegerField()
    version = IntegerVersionField()
    
class Person(models.Model):
    pass

class PersonBook(models.Model):
    pass