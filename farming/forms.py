from django import forms
from .models import SensorData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SensorDataForm(forms.ModelForm):
    class Meta:
        model = SensorData
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

