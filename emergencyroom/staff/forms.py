from django import forms
from .models import Patient, EmergencyContact, Symptom, Medication, Test, Allergy, CovidVaccineShot


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ('first_name', 'last_name', 'patient', 'phone_number')


class PatientNurseForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('doctor_note', 'discharge_instructions', 'bill_due_date')


class PatientDoctorForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('nurse_note', 'bill_due_date')


class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = '__all__'


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = '__all__'


class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'date_of_birth', 'height', 'weight', 'religious_restriction',
                  'drug_usage', 'discharge_instructions', 'gender', 'race', 'sexual_active', 'blood_type')


class SetBillDateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('bill_due_date',)


class CovidShotForm(forms.ModelForm):
    class Meta:
        model = CovidVaccineShot
        fields = '__all__'

