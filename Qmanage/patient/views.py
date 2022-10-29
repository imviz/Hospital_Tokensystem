from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics
from .models import Patient
from .serializer import PatientSerializer


class patient_details(viewsets.ModelViewSet):
    # authentication_classes=[]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
