from rest_framework import serializers
from .models import Patient,Token
from hospital.models import Doctor

class DocterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    doctor=DocterSerializer(many=False)
    class Meta:
        model = Patient
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
    patient=PatientSerializer(many=False)
    class Meta:
        model = Token
        fields = '__all__'
