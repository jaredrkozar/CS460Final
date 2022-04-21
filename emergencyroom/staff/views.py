from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import EmergencyContactForm, SymptomForm, MedicineForm, TestForm, AllergyForm, PatientNurseForm, \
    PatientDoctorForm, CreatePatientForm, SetBillDateForm, CovidShotForm, DiagnoseForm
from .models import Patient, EmergencyContact, Symptom, Test, Diagnose, Medication, Allergy, CovidVaccineShot
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


class PatientListView(LoginRequiredMixin, generic.ListView):
    model = Patient
    context_object_name = 'patient_list'
    paginate_by = 10


@login_required
def patient_view(request, pk):
    patient = Patient.objects.get(pk=pk)
    emergency_contact_list = EmergencyContact.objects.filter(patient=pk)
    symptom_list = Symptom.objects.filter(patient=pk)
    test_list = Test.objects.filter(patient=pk)
    covid_vaccine_list = CovidVaccineShot.objects.filter(patient=pk)
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


@login_required
@permission_required('staff.billing', raise_exception=True)
def bill_form(request, pk):
    if request.method == "GET":
        patient = Patient.objects.get(id=pk)
        form = SetBillDateForm(instance=patient)
        return render(request, 'staff/form_form.html', {'form': form})
    else:
        patient = Patient.objects.get(id=pk)
        form = SetBillDateForm(request.POST, instance=patient)
    if form.is_valid():
        form.save()
    else:
        print('invalid')
    return HttpResponseRedirect('/staff/patient/{}'.format(pk))


@login_required
@permission_required('staff.billing', raise_exception=True)
def print_bill(request, pk):
    patient = Patient.objects.get(pk=pk)
    medication_list = Medication.objects.filter(patient=pk)
    test_list = Test.objects.filter(patient=pk)

    night_cost = patient.nights_stayed * 150
    total_test_cost = 0
    for test in test_list:
        total_test_cost += test.cost
    total_med_cost = 0
    for med in medication_list:
        total_med_cost += med.cost
    total_cost = night_cost + total_med_cost + total_test_cost

    context = {'patient': patient,
               'test_list': test_list,
               'medication_list': medication_list,
               'night_cost': night_cost,
               'total_test_cost': total_test_cost,
               'total_med_cost': total_med_cost,
               'total_cost': total_cost,
               }

    return render(request, 'staff/display_bill.html', context)


@permission_required('staff.not billing', raise_exception=True)
def create_covid_shot_form(request, pk):
    if request.method == "GET":
        intital = {'patient': pk}
        form = CovidShotForm(intital)
        return render(request, 'staff/form_form.html', {'form': form})

    if request.method == 'POST':
        form = CovidShotForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patient/{}'.format(pk))


@login_required()
@permission_required('staff.not billing', raise_exception=True)
def contact_delete(request, pk):
    contact = EmergencyContact.objects.get(id=pk)
    patient_id = contact.patient.pk
    contact.delete()
    return HttpResponseRedirect('/staff/patient/{}'.format(patient_id))


@login_required()
@permission_required('staff.not billing', raise_exception=True)
def vaccine_delete(request, pk):
    model = CovidVaccineShot.objects.get(id=pk)
    patient_id = model.patient.pk
    model.delete()
    return HttpResponseRedirect('/staff/patient/{}'.format(patient_id))


@login_required()
@permission_required('staff.not billing', raise_exception=True)
def allergy_delete(request, pk):
    model = Allergy.objects.get(id=pk)
    patient_id = model.patient.pk
    model.delete()
    return HttpResponseRedirect('/staff/patient/{}'.format(patient_id))


@login_required()
@permission_required('staff.not billing', raise_exception=True)
def symptom_delete(request, pk):
    model = Symptom.objects.get(id=pk)
    patient_id = model.patient.pk
    model.delete()
    return HttpResponseRedirect('/staff/patient/{}'.format(patient_id))


@login_required()
@permission_required('staff.medical professional', raise_exception=True)
def test_delete(request, pk):
    model = Test.objects.get(id=pk)
    patient_id = model.patient.pk
    model.delete()
    return HttpResponseRedirect('/staff/patient/{}'.format(patient_id))


@login_required()
def patient_delete(request, pk):
    model = Patient.objects.get(id=pk)
    model.delete()
    return HttpResponseRedirect('/staff/patients/')


@login_required()
@permission_required('staff.medical professional', raise_exception=True)
def medicine_delete(request, pk):
    model = Medication.objects.get(id=pk)
    patient_id = model.patient.pk
    model.delete()
    return HttpResponseRedirect('/staff/patient/{}'.format(patient_id))


@permission_required('staff.doctor', raise_exception=True)
def create_diagnose_form(request, pk):
    if request.method == "GET":
        intital = {'patient': pk}
        form = DiagnoseForm(intital)
        return render(request, 'staff/form_form.html', {'form': form})

    if request.method == 'POST':
        form = DiagnoseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('invalid')
        return HttpResponseRedirect('/staff/patient/{}'.format(pk))


@login_required()
@permission_required('staff.medical professional', raise_exception=True)
def diagnose_delete(request, pk):
    model = Diagnose.objects.get(id=pk)
    patient_id = model.patient.pk
    model.delete()
    return HttpResponseRedirect('/staff/patient/{}'.format(patient_id))
