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


class TypeService(models.Model):
    title = models.CharField(max_length=50)
    avg_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )
    user = models.ManyToManyField(
        User,
        related_name="rated_services",
        blank=True
    )

    def __str__(self):
        return self.title


class UserTypeService(models.Model):
    class Meta:
        unique_together = ("user", "type_service")

    user = models.ForeignKey(
        User,
        related_name="rated_type_service",
        on_delete=models.SET_DEFAULT,
        default=3
    )
    type_service = models.ForeignKey(
        TypeService,
        on_delete=models.CASCADE,
        related_name="rated_type_service"
    )
    rate = models.PositiveSmallIntegerField()
