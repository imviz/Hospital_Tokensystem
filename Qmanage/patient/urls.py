from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


router=DefaultRouter()
router.register('patient',patient_details,basename='patient')
urlpatterns = [
    
]+router.urls
