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
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        number_of_guests = request.POST.get('number_of_guests')
        date = request.POST.get('date')
        Reservation.objects.create(first_name=first_name, last_name=last_name, number_of_guests=number_of_guests, date=date)

        return redirect('reservations')
    return render(request, 'make_a_reservation.html')
