from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .forms import EmergencyContactForm, SymptomForm, MedicineForm, TestForm, AllergyForm, PatientNurseForm, \
    PatientDoctorForm, CreatePatientForm
from .models import Patient, EmergencyContact, Symptom, Test, Diagnose, Medication, Allergy, CovidVaccineInfo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 10


@login_required
@permission_required('staff.not billing', raise_exception=True)
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


@login_required
@permission_required('staff.registration', raise_exception=True)
def create_patient_form(request):
    if request.method == "GET":
        form = CreatePatientForm()
        return render(request, 'staff/emergencycontact_form.html', {'form': form})

    if request.method == 'POST':
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patients/')


@login_required
@permission_required('staff.registration', raise_exception=True)
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


@login_required
@permission_required('staff.not billing', raise_exception=True)
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


@login_required
@permission_required('staff.doctor', raise_exception=True)
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


@login_required
@permission_required('staff.doctor', raise_exception=True)
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


@login_required
@permission_required('staff.not billing', raise_exception=True)
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


@login_required
@permission_required('staff.nurse', raise_exception=True)
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


@login_required
@permission_required('staff.doctor', raise_exception=True)
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
