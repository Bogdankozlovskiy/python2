from django.shortcuts import render
from sales_manager.models import Book


def main_page(request):
    query_set = Book.objects.all()
    context = {"books": query_set}
    return render(request, "sales_manager/index.html", context=context)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {"book": book}
    return render(request, "sales_manager/book_detail.html", context=context)

