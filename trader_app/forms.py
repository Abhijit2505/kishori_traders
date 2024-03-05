from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
# from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget

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
        widgets = {
            'final_observation':  CKEditorWidget(),
        }

class WindingDataForm(forms.ModelForm):
    class Meta:
        model = WindingData
        fields = '__all__'

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class QuotationSowForm(forms.ModelForm):
    class Meta:
        model = scope_of_work
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'to': CKEditorWidget(),
            'sub': CKEditorWidget(),
            'ref': CKEditorWidget(),
            'scope_of_work': CKEditorWidget(),
            'testing_and_inspection':  CKEditorWidget(),
            'terms_condition':  CKEditorWidget(),
        }

class InspectionReportForm(forms.ModelForm):
    class Meta:
        model = InspectionReport
        fields = '__all__'
        widgets = {
            'to': CKEditorWidget(),
            'sub': CKEditorWidget(),
            'image_captions': CKEditorWidget(),
            'inspection_actual_report': CKEditorWidget(),
            'comments':  CKEditorWidget(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class TestReportDocumentForm(forms.ModelForm):
    class Meta:
        model = TestReportDocument
        fields = '__all__'
        widgets = {
            'motor_details': CKEditorWidget(),
            'jobs_tests_carried_out': CKEditorWidget(),
            'customer_details': CKEditorWidget(),
        }