from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def jobRegister(request):
    form = JobRegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'job_register.html',context=context)

def testReport(request):
    form = TestReportForm()
    context = {
        'form':form,
    }
    return render(request, 'test_report.html',context=context)

def windingData(request):
    form = WindingDataForm()
    context = {
        'form':form,
    }
    return render(request, 'winding_data.html',context=context)

def quotationWithoutSow(request):
    return render(request, 'quotation_without_sow.html')