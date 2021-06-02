from django.urls import path
from hotel import views


urlpatterns = [
    path("filter/", views.filter_room, name="filter-room"),
    path("search/", views.search_room, name="search-room"),
    path("type_service_rate/<int:type_id>/<int:rate>/", views.service_mark, name="type-service-rate"),
]
