from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=124,
        db_index=True,
        verbose_name="название, вот...",
        help_text="вводи пальцами"
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="books"
    )
    date_publish = models.DateField(auto_now_add=True, db_index=True)
    likes = models.ManyToManyField(User, related_name="liked_books", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=3,
        db_index=True,
        related_name="comments"
    )
    like = models.ManyToManyField(User, related_name="liked_comments", blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
