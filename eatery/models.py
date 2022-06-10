from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):

    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return self.first_name