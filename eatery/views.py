from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Reservation


class ReservationList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = 'make_a_reservation.html'


def get_home_page(request):
    return render(request, 'index.html')
