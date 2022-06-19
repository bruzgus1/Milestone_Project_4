from django.db import models
import datetime
from django.contrib.auth.models import User


class Reservation(models.Model):

    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(null=False, blank=False, unique=True)
    number_of_guests = models.IntegerField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False, default=datetime.time(19, 00))
    

    def __str__(self):
        return self.first_name
