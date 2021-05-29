from django.urls import path
from hotel import views


urlpatterns = [
    path("filter/", views.filter_room, name="filter-room"),
    path("search/", views.search_room, name="search-room"),
]
