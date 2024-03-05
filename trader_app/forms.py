from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class JobRegisterForm(forms.ModelForm):
    class Meta:
        model = jobRegister
        fields = '__all__'
        widgets = {
            'in_date': forms.DateInput(attrs={'type': 'date'}),
            'out_date': forms.DateInput(attrs={'type': 'date'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'inspection_photos': forms.ClearableFileInput(attrs={'multiple': True})
        }

class TestReportForm(forms.ModelForm):
    class Meta:
        model = TestReport
        fields = '__all__'

class WindingDataForm(forms.ModelForm):
    class Meta:
        model = WindingData
        fields = '__all__'