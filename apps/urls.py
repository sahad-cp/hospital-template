from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('department',views.department,name='department'),
    path('doctors',views.doctors,name='doctors'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('confirmation',views.confirmation,name='confirmation'),
    
]