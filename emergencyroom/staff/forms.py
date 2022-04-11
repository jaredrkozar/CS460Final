from django import forms
from django.forms import inlineformset_factory
from .models import Patient, EmergencyContact


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ('first_name','last_name','patient','phone_number')


EmergencyContactFormInlineFormset = inlineformset_factory(
    Patient,
    EmergencyContact,
    form=EmergencyContactForm,
    extra=0,
    #max_num=5,
    # fk_name=None,
    # fields=None, exclude=None, can_order=False,
    # can_delete=True, max_num=None, formfield_callback=None,
    # widgets=None, validate_max=False, localized_fields=None,
    # labels=None, help_texts=None, error_messages=None,
    # min_num=None, validate_min=False, field_classes=None
)