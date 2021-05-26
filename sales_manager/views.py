from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from sales_manager.models import Book, Comment
from django.views import View
from sales_manager.utils import get_book_with_comment


def main_page(request):
    query_set = get_book_with_comment()
    context = {"books": query_set}
    return render(request, "sales_manager/index.html", context=context)


def book_detail(request, book_id):
    query_set = get_book_with_comment()
    book = query_set.get(id=book_id)
    context = {"book": book}
    return render(request, "sales_manager/book_detail.html", context=context)


@login_required()
def book_like(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user in book.likes.all():
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
    return redirect("main-page")


class LoginView(View):
    def get(self, request):
        return render(request, "sales_manager/login.html")

    def post(self, request):
        user = authenticate(
            username=request.POST['login'],
            password=request.POST['pwd']
        )
        if user is not None:
            login(request, user)
            return redirect("main-page")
        return redirect("login")


def logout_view(request):
    logout(request)
    return redirect("main-page")


@login_required()
@require_http_methods(["POST"])
def add_comment(request, book_id):
    text = request.POST.get("text")
    Comment.objects.create(
        text=text,
        user_id=request.user.id,
        book_id=book_id
    )
    return redirect("book-detail", book_id=book_id)
