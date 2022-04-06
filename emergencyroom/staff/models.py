from django.core.validators import MinValueValidator
from django.db import models
import datetime
import uuid  # Required for unique book instances
from decimal import Decimal


class Patient(models.model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    date_of_birth = models.DateField(null=True, Blank=True)
    height = models.DoubleField(help_text='Height in cm', validators=[MinValueValidator(Decimal('0.01'))])
    weight = models.DoubleField(help_text='Weight in kg,', validators=[MinValueValidator(Decimal('0.01'))])
    heart_rate = models.PositiveIntegerField(null=True)
    symptoms = models.ManyToManyField('Symptom')
    allergies = models.ManyToManyField('Allergy')


class Symptom(models.model):
    pass


class Allergy(models.model):
    pass


class Test(models.model):
    pass


class Medication(models.model):
    pass


class ReligiousRestrictions(models.model):
    pass


class EmergencyContact(models.model):
    pass


class Diagnose(models.model):
    pass


class CovidVaccineInfo(models.Model):
    pass


class CovidVaccineShot(models.Model):
    pass
