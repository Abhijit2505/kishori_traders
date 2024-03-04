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