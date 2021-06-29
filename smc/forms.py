from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SmcRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'password1', 'password2', 'email', 'phone_number', 'state', 'city', 'school']

class LetterFieldsForm(ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'

class GreivanceForm(ModelForm):
    class Meta:
        model = GrievanceLetter
        fields = ['grievance_letter']