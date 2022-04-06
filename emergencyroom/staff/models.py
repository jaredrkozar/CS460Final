from django.core.validators import MinValueValidator
from django.db import models
import datetime
import uuid  # Required for unique book instances
from decimal import Decimal


class Patient(models.model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    first_name = models.CharField()
    last_name = models.CharField()
    date_of_birth = models.DateField(null=True, Blank=True)
    height = models.DoubleField(help_text='Height in cm', validators=[MinValueValidator(Decimal('0.01'))])
    weight = models.DoubleField(help_text='Weight in kg,', validators=[MinValueValidator(Decimal('0.01'))])
    heart_rate = models.PositiveIntegerField(null=True)
    blood_pressure_upper = models.PositiveIntegerField(null=True)
    blood_pressure_lower = models.PositiveIntegerField(null=True)
    religious_restriction = models.CharField()
    doctor_note = models.CharField(null=True)
    nurse_note = models.CharField(null=True)
    nights_stayed = models.PositiveSmallIntegerField(default=0)
    bill = models.PositiveBigIntegerField()
    drug_usage = models.BooleanField(null=True)
    gender = models.CharField(null=True)
    race = models.CharField(null=True)
    sexual_active = models.BooleanField(null=True)
    blood_type_options = test_options = (
        ('1', 'O negative'),
        ('2', 'O positive'),
        ('3', 'A negative'),
        ('4', 'A positive'),
        ('5', 'B negative'),
        ('6', 'B positive'),
        ('7', 'AB negative'),
        ('8', 'AB  positive'),
    )
    blood_type = models.CharField(max_length=1,
                                  choices=blood_type_options,
                                  blank=True,
                                  )

    class Meta:
        permissions = (('doctor', 'Is a doctor'),
                       ('nurse', 'Is a nurse'),
                       ('medical professional', 'Is a nurse or doctor'),
                       ('billing', 'Is at the billing desk'))


class Symptom(models.model):
    symptom = models.CharField()
    patient = models.ForeignKey('Patient')


class Allergy(models.model):
    allergy = models.CharField()
    patient = models.ForeignKey('Patient')


class Test(models.model):
    test_options = (
        ('A', 'Hematologic Laboratory'),
        ('B', 'Red blood cell '),
        ('C', 'White blood cell'),
        ('D', 'Liver function test'),
        ('E', 'Renal function test'),
        ('F', 'Electrolyte test'),
        ('G', 'Radiologic Laboratory'),
        ('H', 'X-ray'),
        ('I', 'Computed Tomography (CT)'),
        ('J', 'Magnetic Resonance Image (MRI)'),
        ('K', 'Urinary Test'),
        ('L', 'Stool Test'),
    )
    test = models.CharField(max_length=1,
                            choices=test_options)
    patient = models.ForeignKey('Patient')


class Medication(models.model):
    pass


class EmergencyContact(models.model):
    pass


class Diagnose(models.model):
    diagnose_options = (
        ('A', 'Diabetes'),
        ('B', 'Hypertension'),
        ('C', 'Covid'),
        ('D', 'Ammonida'),
        ('E', 'Asthma'),
        ('F', 'Stroke'),
        ('G', 'Heart attack'),
    )
    diagnose = models.CharField(max_length=1,
                                choices=diagnose_options)
    patient = models.ForeignKey('Patient')


class CovidVaccineInfo(models.Model):
    first_shot = models.OneToOneField('CovidVaccineShot')
    second_shot = models.OneToOneField('CovidVaccineShot')
    booster_shot = models.OneToOneField('CovidVaccineShot')
    patient = models.ForeignKey('Patient')


class CovidVaccineShot(models.Model):
    brand_options = (
        ('P', 'Pfizer'),
        ('M', 'Moderna'),
        ('A', 'AstraZeneca'),
        ('J', '	Johnson & Johnson'),
        ('N', 'Novavax'),
        ('R', 'Not taken'),
    )
    brand = models.CharField(max_length=1,
                             choices=brand_options)
    date_received = models.DateField()
