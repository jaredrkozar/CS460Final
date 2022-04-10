from django.shortcuts import render
from django.views import generic

from .models import Patient


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


class PatientListView(generic.ListView):
    model = Patient
    paginate_by = 10
