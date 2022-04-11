from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.patient_view, name='patient-detail'),
    path('newPatient', views.CreatePatient.as_view(), name='new_patient'),
]