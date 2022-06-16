from django import forms
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'number_of_guests', 'date']
        widgets = {
            'first_name': TextInput(attrs={
                'type': 'text',
                'placeholder': 'First Name'}),
            'last_name': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Last Name'}),
            'number_of_guests': NumberInput(attrs={
                'type': 'number',
                'placeholder': '7'}),
            'date': DateTimeInput(attrs={
                'type': 'datetime-local'})
        }