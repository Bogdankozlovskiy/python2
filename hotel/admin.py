from django.contrib import admin
from hotel.models import Room, RoomKind, BookedRoom


admin.site.register(RoomKind)
admin.site.register(Room)
admin.site.register(BookedRoom)
