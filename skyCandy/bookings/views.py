from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking


def landing_page(request):
    return render(request, 'landing_page.html')

def create_booking(request):
    print("booking")
    if request.method == 'POST':
        print("post")
        form = BookingForm(request.POST)
        if form.is_valid():
            print("valid")
            new_booking = form.save(commit=False)
            new_booking.status = 'pending'
            new_booking.save()
            return redirect('booking_success')
        else:
            print("not valid")
    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')
