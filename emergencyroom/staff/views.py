from django.shortcuts import render
from django.views import generic

from .models import Patient
from django import forms

def index(request):
    context = {}
    return render(request, 'index.html', context=context)


class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 10

class PatientDetailView(generic.DetailView):
    model = Patient

