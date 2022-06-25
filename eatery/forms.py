from django import forms
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, TimeInput
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'number_of_guests', 'date', 'time']
        widgets = {
            'first_name': TextInput(attrs={
                'type': 'text',
                'readonly': ''}),
            'number_of_guests': NumberInput(attrs={
                'type': 'number',
                'placeholder': '(min: 1, max: 10)'}),
            'date': DateTimeInput(attrs={
                'type': 'date'}),
            'time': TimeInput(attrs={
                'type': 'time'})
        }
