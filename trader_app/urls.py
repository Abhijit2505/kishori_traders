from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job-register', views.jobRegister, name='job-register'),
    path('test-report', views.testReport, name='test-report'),
    # Add more URL patterns here
]