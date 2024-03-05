from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job-register', views.jobRegister, name='job-register'),
    path('test-report', views.testReport, name='test-report'),
    path('winding-data', views.windingData, name='winding-data'),
    path('quotation-without-sow',views.quotationWithoutSow,name="quotation-without-sow"),
    # Add more URL patterns here
]