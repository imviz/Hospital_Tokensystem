from django.db import models
from hospital.models import Hospital,Doctor

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone =models.CharField(max_length=12)
    doctor = models.ForeignKey(Doctor,on_delete= models.CASCADE)
    hospital = models.ForeignKey(Hospital,on_delete= models.CASCADE)
    
    
    
    def __str__(self):
        return self.name