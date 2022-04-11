from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patient


def index(request):
    context = {}
    return render(request, 'index.html', context=context)

#@login_required
#@permission_required("medical professional", raise_exception=True)
class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 10

class PatientDetailView(generic.DetailView):
    model = Patient


class EditPatient(forms.Form):
    first_name_field = forms.CharField(max_length=20)
    last_name_field = forms.CharField(max_length=20)
    birth_date_field =  forms.DateField(help_text="Enter the patients birth date")
    height_field = forms.DecimalField(min_value=1.0)
    weight_field = forms.IntegerField()
    heart_rate_field = forms.IntegerField()
    blood_pressure_upper_field = forms.IntegerField()
    blood_pressure_lower_field = forms.IntegerField()
    first_name_field = forms.CharField(help_text="enter any religious restrictions this patient has.")
    doctor_note_field = forms.CharField("Doctors notes")
    nurse_note_field = forms.CharField("Nurses notes")
    nights_stayed_field = forms.IntegerField()
    drug_usage_field = forms.BooleanField()
    discharge_instructions_field =  forms.CharField(help_text="Eneter the discharge instructions for this patient")
    gender_field = forms.CharField(help_text="Enter the patients gender")
    race_field = forms.CharField(help_text="Enter the patients gender")
    sexually_active_field = forms.BooleanField()
    IV_field = forms.BooleanField()
    bood_type_field = forms.CharField(help_text="Enter the patients blood type")

