from django.urls import path
from sales_manager import views


urlpatterns = [
    path("", views.main_page)
]
