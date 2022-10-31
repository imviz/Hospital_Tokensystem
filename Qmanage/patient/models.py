from django.db import models
from hospital.models import Hospital, Doctor


class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Token(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    token_no = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    called=models.BooleanField(default=False)

    def __str__(self):
        return self.patient.name
