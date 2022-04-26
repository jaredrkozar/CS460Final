from django.test import TestCase
from django.urls import reverse
from django.test import Client

from .models import Patient
from .models import Symptom
from .models import Allergy
from .models import Medication
from .models import EmergencyContact
from .models import Diagnose
from .models import CovidVaccineShot
from django.utils.timezone import now


def createTestPatient():
    """
    Creates a test patient with first name John and last name Doe
    """

    patient = Patient.objects.create(
        first_name="John",
        last_name="Doe",
        date_of_birth=None,
        bill_due_date=None,
        # insurance_provider="Cigna",
        height=100,
        weight=100,
        blood_pressure_upper=None,
        blood_pressure_lower=None,
        religious_restriction="Hello",
        primary_doctor_name="Mike",
        doctor_note="Needs blood urgently",
        nurse_note="I agree with the doctor",
        nights_stayed=10,
        drug_usage=False,
        race="Indian",
        sexual_active=True,
        IV=True,
        blood_type="1",
        gender="M")
    return patient

#creates a emergency Contact
def createEmergencyContact():
    contact = EmergencyContact.objects.create(
        first_name="Tom",
        last_name="fakeName",
        phone_number=9176561034,
        patient=createTestPatient())
    return contact

class TestPatientModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # create a test patient
        createTestPatient()

    def test_str_is_first_name_and_last_name(self):
        print("Testing _str_ method of patient")
        patient = Patient.objects.get(id=1)
        self.assertEqual(str(patient), f'{patient.last_name}, {patient.first_name}')

    def test_get_absolute_url(self):
        print("Testing patient get_absolute_url")
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_absolute_url(), "/staff/patient/1")

    def test_created_patient(self):
        print("Testing that patient John Doe was created as expected")
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.first_name, "John")
        self.assertEqual(patient.last_name, "Doe")

    def test_get_med(self):
        print("Testing get med link")
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.get_med_link(), "/staff/newMed/1")

    def test_first_name_label(self):
        print("Testing label of first name")
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient._meta.get_field("first_name").verbose_name, "first name")


class TestSymptomModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # create a test patient
        patient = createTestPatient()
        # give the patient a symptom
        Symptom.objects.create(symptom="Dizzines", patient=patient)

    def test_that_patient_has_symptom(self):
        print("Testing that patient has one symptom")
        patient = Patient.objects.get(first_name="John")
        symptoms = Symptom.objects.filter(patient=patient)
        self.assertTrue(len(symptoms) == 1)

    def test_get_delete_url(self):
        print("Testing symptom get_delete_url")
        symptom = Symptom.objects.get(id=1)
        self.assertEqual(symptom.get_delete_url(), "/staff/symptom/1/delete/")


class TestAllergyModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # create a test patient
        patient = createTestPatient()

        Allergy.objects.create(allergy="Pollen", patient=patient)
        Allergy.objects.create(allergy="Wheat", patient=patient)

    def test_that_patient_has_two_allergies(self):
        print("Testing that patient John has two allergies")
        patient = Patient.objects.get(first_name="John")
        allergies = Allergy.objects.filter(patient=patient)
        self.assertTrue(len(allergies) == 2)

    def test_get_delete_url(self):
        print("Testing Allergy get_delete_url")
        allergy = Allergy.objects.get(id=1)
        self.assertEqual(allergy.get_delete_url(), "/staff/allergy/1/delete/")


class TestMedicationModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # create a test patient
        patient = createTestPatient()

        Medication.objects.create(patient=patient, medicine="A", dosage=15.50, cost=100)

    def test_medicine_label(self):
        print("Testing medicine label")
        medicine = Medication.objects.get(id=1)
        self.assertEqual(medicine._meta.get_field("medicine").verbose_name, "medicine")

    def test_patient_given_medication(self):
        print("Testing that patient was given medication")
        patient = Patient.objects.get(id=1)
        medicines = Medication.objects.filter(patient=patient)
        self.assertEqual(len(medicines), 1)
        self.assertEqual(medicines[0].medicine, "A")

    def test_get_delete_url(self):
        print("Testing medication get_delete_url")
        medication = Medication.objects.get(id=1)
        self.assertEqual(medication.get_delete_url(), "/staff/med/1/delete/")


class TestEmergencyContactModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # create a test patient
        patient = createTestPatient()

        # give the patient an emergency contact
        EmergencyContact.objects.create(
            patient=patient,
            first_name="Jane",
            last_name="Doe",
            phone_number="+999999999"
        )

    def test_field_labels(self):
        print("Testing contact field labels")
        contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(contact._meta.get_field("first_name").verbose_name, "first name")
        self.assertEqual(contact._meta.get_field("last_name").verbose_name, "last name")
        self.assertEqual(contact._meta.get_field("phone_number").verbose_name, "phone number")

    def test_contact_name_format(self):
        print("Testing contact name format")
        contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(str(contact), f"{contact.last_name}, {contact.first_name}")

    def test_get_delete_url(self):
        print("Testing EmergencyContact get_delete_url")
        contact = EmergencyContact.objects.get(id=1)
        self.assertEqual(contact.get_delete_url(), "/staff/contact/1/delete/")


class TestDiagnoseModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        patient = createTestPatient()
        # give the patient a diagnosis (Asthma)
        Diagnose.objects.create(
            patient=patient,
            diagnose="E"
        )

    def test_patient_given_diagnosis(self):
        print("Testing that a patient was given correct diagnosis")
        patient = Patient.objects.get(id=1)
        diagnosis = Diagnose.objects.filter(patient=patient)
        self.assertEqual(len(diagnosis), 1, "Patient was not correctly given a diagnosis")
        self.assertEqual(diagnosis[0].diagnose, "E")

    def test_get_delete_url(self):
        print("Testing Diagnose get_delete_url")
        diagnosis = Diagnose.objects.get(id=1)
        self.assertEqual(diagnosis.get_delete_url(), "/staff/diagnose/1/delete/")

class TestCovidVaccineShot(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        patient = createTestPatient()
        CovidVaccineShot.objects.create(
            brand="P",
            date_received=now(),
            patient=patient,
        )

    def test_shot_was_created(self):
        print("Testing that shot was created with brand Pfizer")
        shot = CovidVaccineShot.objects.get(id=1)
        self.assertEqual(shot.brand, "P")

    def test_shot_str(self):
        print("Testing _str_ of shot")
        shot = CovidVaccineShot.objects.get(id=1)
        self.assertTrue(str(shot).startswith("Brand: P"))

    def test_label_of_date_received(self):
        print("Testing label of date_received")
        shot = CovidVaccineShot.objects.get(id=1)
        self.assertEqual(shot._meta.get_field("date_received").verbose_name, "date received")

    def test_get_delete_url(self):
        print("Testing Shot get_delete_url")
        shot = CovidVaccineShot.objects.get(id=1)
        self.assertEqual(shot.get_delete_url(), "/staff/covid_shot/1/delete/")

class TestPatientList(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        # create a test patient
        createTestPatient()

    def index_page_exista(self):
        print("Checking if the index page is available")
        response = self.client.get('index')
        self.assertEqual(response.status_code, 200)

    def all_patients_form_exist(self):
        print("Checking if the add patient form is available")
        response = self.client.get('new_patient')
        self.assertEqual(response.status_code, 400)

    def new_symptom_page_exista(self):
        print("Checking if the new symptom page is available")
        response = self.client.get('new_symptom')
        self.assertEqual(response.status_code, 200)

    def new_medication_page_exista(self):
        print("Checking if the new medication page is available")
        response = self.client.get('new_med')
        self.assertEqual(response.status_code, 200)

    def new_allergy_page_exista(self):
        print("Checking if the new allery page is available")
        response = self.client.get('new_allergy')
        self.assertEqual(response.status_code, 200)

    def bill_form_page_exista(self):
        print("Checking if the new allery page is available")
        response = self.client.get('bill_form')
        self.assertEqual(response.status_code, 200)

    def covid_shot_page_exista(self):
        print("Checking if the new covid shot page is available")
        response = self.client.get('create_covid_shot_form')
        self.assertEqual(response.status_code, 200)

    def covid_shot_page_exista(self):
        print("Checking if the new covid shot page is available")
        response = self.client.get('create_covid_shot_form')
        self.assertEqual(response.status_code, 200)

class TestDeletingObjects(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        # create a test patient
        createEmergencyContact()
        createEmergencyContact()


    def test_deleteEmergencyContact(self):
        c = Client()
        c.post('/login/', {'username': 'doctor1', 'password': 'pw'})
        print("Testing Contact Delete")
        #self.assertEqual(EmergencyContact.objects.count(), 2)
        contact = EmergencyContact.objects.first()
        #print(contact)
        response = c.post('/staff/contact/{}/delete/'.format(contact.id))
        self.assertEqual(EmergencyContact.objects.count(), 2)




