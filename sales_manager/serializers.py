from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from sales_manager.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', "text", "img", "author", "id", "avg_rate"]

    # author = AuthorSerializer()


class RateBookSerializer(serializers.Serializer):
    rate = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    book_id = serializers.IntegerField()

    # def validate_rate(self, instance):
    #     if instance > 5:
    #         raise serializers.ValidationError("rate must be less than 5")
    #     if instance < 0:
    #         raise serializers.ValidationError("rate must be more than 0")
    #     return instance


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', "text", "img", "author", "id"]
