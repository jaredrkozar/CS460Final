from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patient, EmergencyContact, Symptom, Test, Diagnose, Medication, Allergy, CovidVaccineInfo
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


# @login_required
# @permission_required("medical professional", raise_exception=True)
class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 10


def patient_view(request, pk):
    patient = Patient.objects.get(pk=pk)
    emergency_contact_list = EmergencyContact.objects.filter(patient=pk)
    symptom_list = Symptom.objects.filter(patient=pk)
    test_list = Test.objects.filter(patient=pk)
    covid_vaccine_list = CovidVaccineInfo.objects.filter(patient=pk)
    diagnosis_list = Diagnose.objects.filter(patient=pk)
    medication_list = Medication.objects.filter(patient=pk)
    allergy_list = Allergy.objects.filter(patient=pk)

    context = {'patient': patient,
               'emergency_contact_list': emergency_contact_list,
               'symptom_list': symptom_list,
               'test_list': test_list,
               'covid_vaccine_list': covid_vaccine_list,
               'diagnosis_list': diagnosis_list,
               'medication_list': medication_list,
               'allergy_list': allergy_list
               }
    return render(request, 'staff/patient_detail.html', context)


class CreatePatient(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'height', 'weight', 'heart_rate', 'blood_pressure_upper',
              'blood_pressure_lower', 'religious_restriction', 'doctor_note', 'nurse_note', 'nights_stayed',
              'drug_usage', 'discharge_instructions', 'gender', 'race', 'sexual_active', 'IV', 'blood_type']
