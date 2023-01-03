from django.contrib import admin
from .models import Booking,Departments,Doctors
# Register your models here.


admin.site.register(Booking)
admin.site.register(Departments)
admin.site.register(Doctors)