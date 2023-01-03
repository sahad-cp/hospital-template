from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    
    def __str__(self) :
        return self.dep_name
    
class Doctors(models.Model):
    doc_name = models.CharField(max_length=225)
    dep_name = models.ForeignKey(Departments, on_delete= models.CASCADE)
    doc_image = models.ImageField( upload_to='doctors')

    def __str__(self):
        return 'Dr ' + self.doc_name 




class Booking(models.Model):
    fullName = models.CharField(max_length=225)
    place = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()