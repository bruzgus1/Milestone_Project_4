from django import forms
from django.forms import ModelForm, TextInput, NumberInput, DateInput, Select
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_under', 'number_of_guests',
                  'date_of_reservation', 'time']
        widgets = {
            'reservation_under': TextInput(attrs={
                'type': 'text',
                'readonly': ''}),
            'number_of_guests': NumberInput(attrs={
                'type': 'number',
                'placeholder': '(min: 1, max: 10)'}),
            'date_of_reservation': DateInput(attrs={
                'type': 'date'}),
            'time': Select(attrs={'class': 'select'})
        }
