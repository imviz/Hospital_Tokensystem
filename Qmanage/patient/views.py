from token import tok_name
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


# docter token creation 
@api_view(['POST'])
def token_creation(request):
    try:
        data = request.data
        patient = data['patient']
        doctor = data['doctor']
        hospital = data['hospital']
        check=Token.objects.filter(doctor_id=doctor, hospital_id=hospital,patient=patient).exists()
        if not check:
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
        else:
            message = {'detail': 'this patient is already take a token'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


    except:
        message = {'detail': 'token error'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


# docter token calling
@api_view(['GET'])
def call_token(request, hospital, doctor):
    token = Token.objects.filter(
        doctor=doctor, hospital=hospital, called=False).order_by('token_no')[:1]

    serializer = TokenSerializer(token, many=True)
    print(serializer.data)
    for i in serializer.data:
        tok_id = i['token_no']
    token = Token.objects.get(
        hospital=hospital, doctor=doctor, token_no=tok_id)
    token.called = True
    token.save()
    return Response(serializer.data)


# token check for patient
@api_view(['POST'])
def patient_check(request):
    data=request.data
    hospital=data['hospital']
    doctor=data['doctor']
    mobile=data['mobile']
    check=Token.objects.filter(hospital=hospital,doctor=doctor,patient__phone=mobile,called=False).exists()
    if check:
        print('ok')
        
        # otp sending
        
        token=Token.objects.get(hospital=hospital,doctor=doctor,patient__phone=mobile,called=True)
        serializer=TokenSerializer(token,many=False)
        return Response(serializer.data)
    else:
        print('no')
        return Response({'no'})
    
    
    
#otp checking






#personal token with estimate time /current/own token
@api_view(['GET'])
def patient_token(request,id):
    token=Token.objects.get(id=id)
    your_token_no=token.token_no
    hospital=token.hospital
    doctor=token.doctor
    check=Token.objects.filter(hospital=hospital,doctor=doctor,called=True)[:1].exists()
    token=Token.objects.filter(hospital=hospital,doctor=doctor,called=False).order_by('token_no')[:1]
    current_token=0
    if check:
        for i in token:
            token_id=i.token_no       
        current_token=token_id
        check2=Token.objects.filter(hospital=hospital,doctor=doctor,called=True)[1:2].exists()
    estimate_time=0
    if check:
        tokenz=Token.objects.filter(hospital=hospital,doctor=doctor,called=True).order_by('-token_no')[:1]
        for j in tokenz:
            modified1=j.modified                                        
    if check2:   
        tokenq=Token.objects.filter(hospital=hospital,doctor=doctor,called=True).order_by('-token_no')[1:2]   
        for i in tokenq:
            modified2=i.modified 
            estimate_time=(modified1-modified2)/60     
            waiting_time=(((your_token_no-current_token)-1)*estimate_time/60)*100
            print(waiting_time,'000k')
    context={
        'current_token':current_token,
        'your_token':your_token_no,
        'time_taken_for last_token':estimate_time,
        'waiting_time':waiting_time,
    }     
    return Response(context)