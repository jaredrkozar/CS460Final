from django import forms
from django.forms import inlineformset_factory
from .models import Patient, EmergencyContact, Symptom, Medication


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ('first_name','last_name','patient','phone_number')


class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = '__all__'


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'

