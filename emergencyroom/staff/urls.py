from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('newPatient', views.create_patient_form, name='new_patient'),
    path('patient/<int:pk>', views.patient_view, name='patient-detail'),
    path('newContact/<int:pk>', views.emergency_contact_form, name='new_contact'),
    path('newSymptom/<int:pk>', views.symptom_form, name='new_symptom'),
    path('newMed/<int:pk>', views.medicine_form, name='new_med'),
    path('newTest/<int:pk>', views.test_form, name='new_test'),
    path('newAllergy/<int:pk>', views.allergy_form, name='new_allergy'),
    path('patient_nurse/<int:pk>', views.patient_nurse_form, name='patient_nurse_form'),
    path('patient_doctor/<int:pk>', views.patient_doctor_form, name='patient_doctor_form'),
    path('patient_bill/<int:pk>', views.bill_form, name='bill_form'),
    path('patient_bill_display/<int:pk>', views.print_bill, name='print_bill'),
    path('covid_shot/<int:pk>', views.create_covid_shot_form, name='create_covid_shot_form'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)