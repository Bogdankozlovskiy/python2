from django.shortcuts import render
from hotel.models import RoomKind, Room, BookedRoom
from django.db.models import Q
from datetime import datetime


def filter_room(request):
    rk = RoomKind.objects.all()
    return render(request, "hotel/index.html", {"kinds": rk})


def search_room(request):
    start_date = datetime.strptime(request.GET['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(request.GET['end_date'], "%Y-%m-%d")
    kind = request.GET['kind']
    br = BookedRoom.objects.filter(
        Q(start_date__gte=start_date, end_date__lte=end_date) |
        Q(start_date__lte=start_date, end_date__gte=end_date) |
        Q(start_date__gte=start_date, start_date__lte=end_date, end_date__gte=end_date) |
        Q(end_date__gte=start_date, end_date__lte=end_date, start_date__lte=end_date)
    )
    rooms = Room.objects.filter(~Q(booked__in=br) & Q(kind=kind))
    return render(request, "hotel/search.html", {"rooms": rooms})
