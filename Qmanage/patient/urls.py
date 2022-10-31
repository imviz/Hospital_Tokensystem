from django import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from . import views


router=DefaultRouter()
router.register('patient',patient_details,basename='patient')
urlpatterns = [
    path('token/create/',views.token_creation,name='token-creation'),
    path('token/call/<int:hospital>/<int:doctor>/',views.call_token,name='call-token'),
    path('token/check/',views.patient_check,name='check-token'),
    path('token/patient/<int:id>/',views.patient_token,name='patient-token'),
    
]+router.urls
