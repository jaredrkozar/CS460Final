# Generated by Django 4.0.4 on 2022-04-12 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_alter_patient_iv'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('doctor', 'Is a doctor'), ('nurse', 'Is a nurse'), ('medical professional', 'Is a nurse or doctor'), ('billing', 'Is at the billing desk'), ('registration', 'is a registrar desk'), ('not billing', 'is not billing'))},
        ),
    ]