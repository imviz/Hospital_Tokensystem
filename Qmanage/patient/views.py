from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, generics, status
from .models import Patient, Token
from .serializer import PatientSerializer, TokenSerializer
from hospital.models import Hospital


class patient_details(viewsets.ModelViewSet):
    # authentication_classes=[]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


@api_view(['POST'])
def token_creation(request):
    try:
        data = request.data
        patient = data['patient']
        doctor = data['doctor']
        hospital = data['hospital']
        doct = Token.objects.filter(doctor_id=doctor, hospital_id=hospital)
        token = len(doct)+1
        tokenz = Token.objects.create(
            patient_id=patient,
            doctor_id=doctor,
            hospital_id=hospital,
            token_no=token
        )
        serializer = TokenSerializer(tokenz, many=False)
        return Response(serializer.data)

    except:
        message = {'detail': 'token error'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
