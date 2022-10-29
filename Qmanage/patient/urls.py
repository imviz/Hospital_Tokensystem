from django import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from . import views


router=DefaultRouter()
router.register('patient',patient_details,basename='patient')
urlpatterns = [
    path('token/create/',views.token_creation,name='token-creation')
]+router.urls
