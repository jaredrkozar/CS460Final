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

