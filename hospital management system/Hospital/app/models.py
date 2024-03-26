from typing import Any
from django.db import models
class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=50)
    address = models.TextField()
    
    
    def __str__(self):
        return self.patient_name
