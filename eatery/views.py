from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from .models import Reservation


class reservation_list(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    context_object_name = 'reservations'
    template_name = 'reservations.html'


def get_home_page(request):
    return render(request, 'index.html')


def make_reservation(request):
    return render(request, 'make_a_reservation.html')
