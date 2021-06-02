from django.contrib import admin
from hotel.models import Room, RoomKind, BookedRoom, TypeService


class TypeServiceAdmin(admin.ModelAdmin):
    exclude = ("user", )
    readonly_fields = ("avg_rate", )


admin.site.register(RoomKind)
admin.site.register(Room)
admin.site.register(BookedRoom)
admin.site.register(TypeService, TypeServiceAdmin)
