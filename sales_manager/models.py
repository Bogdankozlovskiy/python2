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
    likes = models.ManyToManyField(User, related_name="liked_books")

    def __str__(self):
        return self.title
