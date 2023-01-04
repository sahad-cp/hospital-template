from django.contrib import admin
from .models import Booking,Departments,Doctors
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','fullName','email','doc_name','booking_date')

admin.site.register(Booking,BookingAdmin)
admin.site.register(Departments)
admin.site.register(Doctors)