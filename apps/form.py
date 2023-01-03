from django import forms
from .models import Booking

class Appointment(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

