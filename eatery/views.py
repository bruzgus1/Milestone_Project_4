from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import Reservation
from .forms import ReservationForm


class reservation_list(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    context_object_name = 'reservations'
    template_name = 'reservations.html'


def get_home_page(request):
    return render(request, 'index.html')


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    form = ReservationForm()
    context = {
        'form': form
    }
    return render(request, 'make_a_reservation.html', context)


def edit_reservation(request, i_id):
    reservation = get_object_or_404(Reservation, id=i_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'edit_reservation.html', context)


def delete_reservation(request, i_id):
    reservation = get_object_or_404(Reservation, id=i_id)
    reservation.delete()
    return redirect('reservations')
