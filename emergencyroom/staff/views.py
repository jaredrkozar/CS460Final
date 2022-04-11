from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patient
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class CreatePatient(CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'date_of_birth', 'height', 'weight', 'heart_rate', 'blood_pressure_upper', 'blood_pressure_lower', 'religious_restriction', 'doctor_note', 'nurse_note', 'nights_stayed', 'drug_usage', 'discharge_instructions', 'gender', 'race', 'sexual_active', 'IV', 'blood_type']

