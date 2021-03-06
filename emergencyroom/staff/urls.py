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
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact-delete'),
    path('covid_shot/<int:pk>/delete/', views.vaccine_delete, name='covid_shot-delete'),
    path('allergy/<int:pk>/delete/', views.allergy_delete, name='allergy-delete'),
    path('symptom/<int:pk>/delete/', views.symptom_delete, name='symptom-delete'),
    path('test/<int:pk>/delete/', views.test_delete, name='test-delete'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient-delete'),
    path('med/<int:pk>/delete/', views.medicine_delete, name='medicine-delete'),
    path('diagnose/<int:pk>', views.create_diagnose_form, name='create_diagnose_form'),
    path('diagnose/<int:pk>/delete/', views.diagnose_delete, name='diagnose-delete'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)