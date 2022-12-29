from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def department(request):
    return render(request,'department.html')
def doctors(request):
    return render(request,'doctors.html')
def booking(request):
    return render(request,'booking.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')
def confirmation(request):
    return render(request,'confirmation.html')