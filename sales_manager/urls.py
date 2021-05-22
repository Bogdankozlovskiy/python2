from django.urls import path
from sales_manager import views


urlpatterns = [
    path("book_detail/<int:book_id>/", views.book_detail, name="book-detail"),
    path("book_like/<int:book_id>/", views.book_like, name="book-like"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.main_page, name="main-page"),
]
