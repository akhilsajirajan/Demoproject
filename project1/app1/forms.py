from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class Dateinput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': Dateinput(),
        }

        labels = {
            'p_name' : 'Patient Name: ',
            'p_phone' : 'Patient Phone: ',
            'p_email' : 'Patient Email: ',
            'booking_date': 'Booking Date: ',
        }

class Doctorsform(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'
        
        
        labels = {
            'doc_name': "Doctors Name: ",
            'doc_spec' : "Doctors Specification:",
            'dep_name' : "Department Name",
            
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')