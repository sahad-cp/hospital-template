from django.shortcuts import render
from .models import Departments,Doctors
from .form import Appointment

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')



def department(request):
    dict_dept ={
        'dept' : Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)





def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)






def services(request):
    return render(request,'services.html')





def contact(request):
    if request.method == "POST":
        form = Appointment(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
        
    form = Appointment()
    dict_form = {
        'form': form
    }    
    return render(request,'contact.html',dict_form)




def confirmation(request):
    return render(request,'confirmation.html')