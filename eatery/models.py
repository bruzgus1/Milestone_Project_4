from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime
from datetime import timedelta


class Reservation(models.Model):

    TIMES = (
        ('12:00', '12:00'),
        ('14:00', '14:00'),
        ('17:00', '17:00'),
        ('19:00', '19:00'),
        ('21:00', '21:00'),
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    reservation_under = models.CharField(max_length=200, null=False, blank=False)
    date_of_reservation = models.DateField(null=False, blank=False, unique=True, validators=
    [MinValueValidator(datetime.date.today() + timedelta(days=1))])
    number_of_guests = models.IntegerField(null=False, blank=False, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    time = models.CharField(null=False, blank=False,default='19:00', choices=TIMES, max_length=5)

    def __str__(self):
        return self.reservation_under
