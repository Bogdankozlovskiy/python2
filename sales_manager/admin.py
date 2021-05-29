from django.contrib import admin
from sales_manager.models import Book, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment
    readonly_fields = ("like", )


class BookInline(admin.ModelAdmin):
    inlines = (CommentAdmin, )
    # readonly_fields = ("likes", )
    list_filter = ("date_publish", "author")
    # list_editable = ("title", )
    list_display = ("title", "date_publish", )
    # list_display_links = ("text", )


admin.site.register(Book, BookInline)
