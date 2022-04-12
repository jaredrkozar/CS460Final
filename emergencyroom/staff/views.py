from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import EmergencyContactForm, SymptomForm, MedicineForm, TestForm, AllergyForm, PatientNurseForm, \
    PatientDoctorForm
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


class CreatePatientView(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'height', 'weight', 'heart_rate', 'blood_pressure_upper',
              'blood_pressure_lower', 'religious_restriction', 'doctor_note', 'nurse_note', 'nights_stayed',
              'drug_usage', 'discharge_instructions', 'gender', 'race', 'sexual_active', 'IV', 'blood_type']


class CreateEmergencyContact(CreateView):
    model = EmergencyContact
    fields = '__all__'

    def get_context_data(self, **kwargs):
        ctx = super(CreateEmergencyContact, self).get_context_data(**kwargs)
        ctx['patient'] = self.pk
        return ctx


def emergency_contact_form(request, pk):
    if request.method == "GET":
        intital = {'patient': pk}
        form = EmergencyContactForm(intital)
        return render(request, 'staff/emergencycontact_form.html', {'form': form})

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patient/{}'.format(pk))


def symptom_form(request, pk):
    if request.method == "GET":
        intital = {'patient': pk}
        form = SymptomForm(intital)
        return render(request, 'staff/form_form.html', {'form': form})

    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patient/{}'.format(pk))


def medicine_form(request, pk):
    if request.method == "GET":
        intital = {'patient': pk}
        form = MedicineForm(intital)
        return render(request, 'staff/form_form.html', {'form': form})

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patient/{}'.format(pk))


def test_form(request, pk):
    if request.method == "GET":
        intital = {'patient': pk}
        form = TestForm(intital)
        return render(request, 'staff/form_form.html', {'form': form})

    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patient/{}'.format(pk))


def allergy_form(request, pk):
    if request.method == "GET":
        intital = {'patient': pk}
        form = AllergyForm(intital)
        return render(request, 'staff/form_form.html', {'form': form})

    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patient/{}'.format(pk))


def patient_nurse_form(request, pk):
    if request.method == "GET":
        patient = Patient.objects.get(id=pk)
        form = PatientNurseForm(instance=patient)
        return render(request, 'staff/form_form.html', {'form': form})

    else:
        patient = Patient.objects.get(id=pk)
        form = PatientNurseForm(request.POST, instance=patient)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect('/staff/patient/{}'.format(pk))


def patient_doctor_form(request, pk):
    if request.method == "GET":
        patient = Patient.objects.get(id=pk)
        form = PatientDoctorForm(instance=patient)
        return render(request, 'staff/form_form.html', {'form': form})

    else:
        patient = Patient.objects.get(id=pk)
        form = PatientDoctorForm(request.POST, instance=patient)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect('/staff/patient/{}'.format(pk))
