from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.patient_view, name='patient-detail'),
    path('newPatient', views.CreatePatientView.as_view(), name='new_patient'),
    path('newContact/<int:pk>', views.emergency_contact_form, name='new_contact'),
    path('newSymptom/<int:pk>', views.symptom_contact_form, name='new_symptom'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)