from django.db import models

class book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  genre = models.CharField(max_length=50)
  puplication_date = models.DateField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  def __str__(self):
    return self.title
    # we need to create a view that will render our HTML template with 
    from Django.shortcuts import render
    from.models import book

def book_list(request):
  books = Book.objects.all()
  return render(request, 'books/book_list.html', {'books':}
                                                  
  #create the HTML template. Create a folder called templates 
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bookstore</title>
</head>
  
