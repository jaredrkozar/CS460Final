from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
import uuid
from decimal import Decimal
from django.urls import reverse
from django.core.validators import RegexValidator


class Patient(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    insurance_provider = models.CharField(max_length=40, null=True, blank=True)
    primary_doctor_name = models.CharField(max_length=40, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.FloatField(help_text='Height in cm', validators=[MinValueValidator(Decimal('0.01'))], null=True, blank=True)
    weight = models.FloatField(help_text='Weight in kg,', validators=[MinValueValidator(Decimal('0.01'))],  null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True,  blank=True)
    blood_pressure_upper = models.PositiveIntegerField(null=True,  blank=True)
    blood_pressure_lower = models.PositiveIntegerField(null=True,  blank=True)
    religious_restriction = models.TextField( blank=True)
    doctor_note = models.TextField(null=True, blank=True)
    nurse_note = models.TextField(null=True, blank=True)
    nights_stayed = models.PositiveSmallIntegerField(default=0, blank=True)
    # bill = models.PositiveBigIntegerField()
    drug_usage = models.BooleanField(null=True, blank=True)
    discharge_instructions = models.TextField(null=True, blank=True)
    gender_options = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1,
                              choices=gender_options,
                              blank=True, )
    race = models.CharField(null=True, max_length=20, blank=True)
    sexual_active = models.BooleanField(null=True, blank=True)
    IV = models.BooleanField(null=True, blank=True)
    blood_type_options = (
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

    # doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bill_due_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = (('doctor', 'Is a doctor'),
                       ('nurse', 'Is a nurse'),
                       ('medical professional', 'Is a nurse or doctor'),
                       ('billing', 'Is at the billing desk'),
                       ('registration', 'is a registrar desk'),
                       ('not billing', 'is not billing'))
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('patient-detail', args=[str(self.id)])

    def get_contact_link(self):
        return reverse('new_contact', args=[str(self.id)])

    def get_symptom_link(self):
        return reverse('new_symptom', args=[str(self.id)])

    def get_med_link(self):
        return reverse('new_med', args=[str(self.id)])

    def get_test_link(self):
        return reverse('new_test', args=[str(self.id)])

    def get_diagnose_link(self):
        return reverse('create_diagnose_form', args=[str(self.id)])

    def get_allergy_link(self):
        return reverse('new_allergy', args=[str(self.id)])

    def get_nurse_url(self):
        return reverse('patient_nurse_form', args=[str(self.id)])

    def get_doctor_url(self):
        return reverse('patient_doctor_form', args=[str(self.id)])

    def get_bill_form_url(self):
        return reverse('bill_form', args=[str(self.id)])

    def get_bill_display_url(self):
        return reverse('print_bill', args=[str(self.id)])

    def get_covid_shot_url(self):
        return reverse('create_covid_shot_form', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    def get_delete_url(self):
        return reverse('patient-delete', args=[str(self.id)])


class Symptom(models.Model):
    symptom = models.CharField(max_length=20)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse('symptom-delete', args=[str(self.id)])


class Allergy(models.Model):
    allergy = models.CharField(max_length=20)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse('allergy-delete', args=[str(self.id)])

class Test(models.Model):
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
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    cost = models.FloatField(help_text='', validators=[MinValueValidator(Decimal('0.01'))])

    def get_delete_url(self):
        return reverse('test-delete', args=[str(self.id)])

class Medication(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    medicine_options = (
        ('A', 'Insulin'),
        ('B', 'Candesartan'),
        ('C', 'Dexamethasone'),
        ('D', 'Azithromycin'),
        ('E', 'Fluticasone'),
        ('F', 'Alteplase'),
        ('G', 'Aspirin'),
    )

    medicine = models.CharField(max_length=1,
                                choices=medicine_options, null=False)
    dosage = models.FloatField(help_text='Dosage in mg', validators=[MinValueValidator(Decimal('0.01'))])
    cost = models.FloatField(help_text='', validators=[MinValueValidator(Decimal('0.01'))])

    def get_delete_url(self):
        return reverse('medicine-delete', args=[str(self.id)])


class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    def get_delete_url(self):
        return reverse('contact-delete', args=[str(self.id)])


class Diagnose(models.Model):
    diagnose_options = (
        ('A', 'Diabetes'),
        ('B', 'Hypertension'),
        ('C', 'Covid'),
        ('D', 'Pneumonia'),
        ('E', 'Asthma'),
        ('F', 'Stroke'),
        ('G', 'Heart attack'),
    )
    diagnose = models.CharField(max_length=1,
                                choices=diagnose_options)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def get_delete_url(self):
        return reverse('diagnose-delete', args=[str(self.id)])


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
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)

    def __str__(self):
        return 'Brand: {brand} \n Date Recieved: {date}'.format(brand=self.brand, date=self.date_received)

    def get_delete_url(self):
        return reverse('covid_shot-delete', args=[str(self.id)])
