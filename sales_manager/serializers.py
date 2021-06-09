from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField

from sales_manager.models import Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name"]


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', "text", "img", "author", "id"]

    # author = AuthorSerializer()
