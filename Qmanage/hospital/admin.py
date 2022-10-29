from django.contrib import admin
from .models import * 
from patient.models import Patient
# Register your models here.
admin.site.register(Hospital)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Doctor)
admin.register(Patient)