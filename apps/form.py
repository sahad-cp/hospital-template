from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class Appointment(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets ={
            'booking_date' : DateInput(attrs={'class':'form-control'}),
            'fullName':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'doc_name':forms.TextInput(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        labels = {
            'fullName':"Patient Name:",
            'number': "Patient Phone:",
            'email': "Patient Email:",
            'doc_name': "Doctor Name:",
            'booking_date': "Booking Date:",
        }
