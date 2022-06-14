from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


def get_home_page(request):
    return render(request, 'index.html')


def get_reversation_page(request):
    return render(request, 'make_a_reservation.html')
