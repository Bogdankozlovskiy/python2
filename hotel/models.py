from django.db import models
from django.contrib.auth.models import User


class RoomKind(models.Model):
    name = models.CharField(max_length=10, primary_key=True)


class Room(models.Model):
    description = models.TextField()
    kind = models.ForeignKey(RoomKind, on_delete=models.CASCADE)
    user = models.ManyToManyField(
        User,
        through="BookedRoom",
        related_name="room"
    )


class BookedRoom(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="booked"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booked"
    )
