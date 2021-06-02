from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from hotel.models import RoomKind, Room, BookedRoom, TypeService, UserTypeService
from django.db.models import Q, Avg
from datetime import datetime


def filter_room(request):
    rk = RoomKind.objects.all()
    ts = TypeService.objects.all()
    return render(request, "hotel/index.html", {"kinds": rk, "types": ts})


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


@login_required()
def service_mark(request, type_id, rate):
    UserTypeService.objects.update_or_create(
        user_id=request.user.id,
        type_service_id=type_id,
        defaults={"rate": rate}
    )
    ts = TypeService.objects.get(id=type_id)
    ts.avg_rate = ts.rated_type_service.aggregate(rate=Avg("rate"))['rate']
    ts.save(update_fields=['avg_rate'])
    return redirect("filter-room")
