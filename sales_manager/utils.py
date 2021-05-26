from django.db.models import Count, Prefetch
from sales_manager.models import Comment, Book


def get_book_with_comment():
    comment_query = Comment.objects.all().select_related("user"). \
        annotate(count_likes=Count("like"))
    comment_prefetch = Prefetch("comments", queryset=comment_query)
    query_set = Book.objects.all().select_related("author"). \
        prefetch_related(comment_prefetch).annotate(count_likes=Count("likes"))
    return query_set
