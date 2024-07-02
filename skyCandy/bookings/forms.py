from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['package', 'date', 'time_slot', 'customer_name', 'customer_email', 'customer_phone', 'participants']
