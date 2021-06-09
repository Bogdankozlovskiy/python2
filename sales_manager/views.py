from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework import pagination
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from sales_manager.models import Book, Comment, UserRateBook
from django.views import View
from sales_manager.serializers import BookSerializer
from sales_manager.utils import get_book_with_comment
from rest_framework import filters


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
def book_like(request, book_id, rate, redirect_url):
    UserRateBook.objects.update_or_create(
        user_id=request.user.id,
        book_id=book_id,
        defaults={"rate": rate}
    )
    book = Book.objects.get(id=book_id)
    book.avg_rate = book.rated_user.aggregate(rate=Avg("rate"))['rate']
    book.save(update_fields=["avg_rate"])
    if redirect_url == "main-page":
        return redirect("main-page")
    elif redirect_url == "book-detail":
        return redirect("book-detail", book_id=book_id)


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


@login_required()
def comment_like(request, comment_id):
    com = Comment.objects.get(id=comment_id)
    if request.user in com.like.all():
        com.like.remove(request.user)
    else:
        com.like.add(request.user)
    return redirect("book-detail", book_id=com.book_id)


def add_like_ajax(request):
    comment_id = request.POST['comment_id']
    query_com = Comment.objects.filter(id=comment_id)
    if query_com.exists():
        com = query_com.first()
        if request.user in com.like.all():
            com.like.remove(request.user)
        else:
            com.like.add(request.user)
        return HttpResponse(com.like.count())
    return HttpResponseNotFound("error")


# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all().select_related("author")
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [BasicAuthentication, TokenAuthentication]

# class BookListAPIView(APIView):
#     def get(self, request):
#         query_set = Book.objects.all()
#         serializer = BookSerializer(query_set, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             book = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyPagination(pagination.LimitOffsetPagination):
    max_limit = 2


class BookListAPIView(ListCreateAPIView):
    pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ['id', 'title']
    ordering = ['-id']
    search_fields = ('title', 'text')


class BookDetail(GenericAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer

    def get(self, request, pk):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data)

# CRUD
# GET, Options
# Put Putch Delete Post


class BookUpdateAPI(RetrieveUpdateDestroyAPIView):
    '''hello'''
    queryset = Book.objects
    serializer_class = BookSerializer


