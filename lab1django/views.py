from lab1django.models import Book
from django.shortcuts import render

# Create your views here.
def main_page(request):
    all_books = Book.objects.order_by("publication_date")
    ctx = {"books":(all_books)}
    return render(request,'lab1django/index.html',ctx)
