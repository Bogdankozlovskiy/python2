from django.urls import path
from sales_manager import views


urlpatterns = [
    path("book_detail/<int:book_id>/", views.book_detail, name="book-detail"),
    path("", views.main_page),
]
