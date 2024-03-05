from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job-register', views.jobRegister, name='job-register'),
    path('test-report', views.testReport, name='test-report'),
    path('winding-data', views.windingData, name='winding-data'),
    path('quotation-without-sow',views.quotationWithoutSow,name="quotation-without-sow"),
    path('inspection-report',views.inspectionReport,name="inspection-report"),
    path('sow-quotation',views.quotationWithSow,name="sow-quotation"),
    path('test-report-document',views.testReportDocument,name="test-report-document"),
    # Add more URL patterns here
]