from django.contrib import admin
from django.urls import path,include
from dashboard import views

urlpatterns = [
    
    path('dashboard/home',views.Home,name='dash_home'),
    path('dashboard/booking',views.Home,name='dash_booking'),
    path('dashboard/department',views.Home,name='dash_department'),
    path('dashboard/doctor',views.Home,name='dash_doctor'),
    
    
]