from django.shortcuts import render
from .models import Book

def index(request):
    num_books = Book.objects.all().count()
    return render(request, 'index.html', context={'num_books': num_books})
