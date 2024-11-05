from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} : {self.price:.2f}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self) -> str:
        return (
            f"{self.user.username} : {self.booking_date} - {self.no_of_guests} guest(s)"
        )
