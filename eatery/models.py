from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):

    first_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    last_name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    number_of_guests = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.first_name
