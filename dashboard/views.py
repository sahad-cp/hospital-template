from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'d-index.html')


def booking(request):
    return render(request,'d-booking.html')


def department(request):
    return render(request,'d-department.html')


def doctor(request):
    return render(request,'d-doctor.html')