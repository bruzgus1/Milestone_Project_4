from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import get_user
from django.contrib import messages
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
        form.instance.created_by = request.user
        if form.is_valid():
            form.save()
            messages.success(request, "Your Reservation Was Submitted")
            return redirect('reservations')
        else:
            messages.error(request, "Your Reservation Was Not Submitted,",
                                    "Double Check All The Fields And Try Again"
                           )
    else:
        # Get the currently logged-in User.
        user = get_user(request)
        # Provide User as initial data to the form
        form = ReservationForm(initial={'reservation_under': user})
    context = {
        'form': form,
        'reservations': Reservation.objects.all()
    }
    return render(request, 'make_a_reservation.html', context)


def edit_reservation(request, i_id):
    reservation = get_object_or_404(Reservation, id=i_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Reservation Was Updated")
            return redirect('reservations')
        else:
            messages.error(request, "Your Reservation Was Not Updated,",
                                    "Double Check All The Fields And Try Again"
                           )
    form = ReservationForm(instance=reservation)
    context = {
        'form': form,
        'reservations': Reservation.objects.all()
    }
    return render(request, 'edit_reservation.html', context)


def delete_reservation(request, i_id):
    reservation = get_object_or_404(Reservation, id=i_id)
    reservation.delete()
    messages.success(request, "Your Reservation Was Deleted Successfully")
    return redirect('reservations')
