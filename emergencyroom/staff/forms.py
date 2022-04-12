from django import forms
from django.forms import inlineformset_factory
from .models import Patient, EmergencyContact, Symptom, Medication, Test, Allergy


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ('first_name','last_name','patient','phone_number')

class PatientNurseForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude =  ('doctor_note','discharge_instructions')

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
