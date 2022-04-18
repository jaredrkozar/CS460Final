# Generated by Django 4.0.4 on 2022-04-11 22:53

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidVaccineShot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('P', 'Pfizer'), ('M', 'Moderna'), ('A', 'AstraZeneca'), ('J', '\tJohnson & Johnson'), ('N', 'Novavax'), ('R', 'Not taken')], max_length=1)),
                ('date_received', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField(null=True)),
                ('height', models.FloatField(help_text='Height in cm', validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('weight', models.FloatField(help_text='Weight in kg,', validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('heart_rate', models.PositiveIntegerField(null=True)),
                ('blood_pressure_upper', models.PositiveIntegerField(null=True)),
                ('blood_pressure_lower', models.PositiveIntegerField(null=True)),
                ('religious_restriction', models.TextField()),
                ('doctor_note', models.TextField(null=True)),
                ('nurse_note', models.TextField(null=True)),
                ('nights_stayed', models.PositiveSmallIntegerField(default=0)),
                ('drug_usage', models.BooleanField(null=True)),
                ('discharge_instructions', models.TextField(null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('race', models.CharField(max_length=20, null=True)),
                ('sexual_active', models.BooleanField(null=True)),
                ('IV', models.BooleanField()),
                ('blood_type', models.CharField(blank=True, choices=[('1', 'O negative'), ('2', 'O positive'), ('3', 'A negative'), ('4', 'A positive'), ('5', 'B negative'), ('6', 'B positive'), ('7', 'AB negative'), ('8', 'AB  positive')], max_length=1)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'permissions': (('doctor', 'Is a doctor'), ('nurse', 'Is a nurse'), ('medical professional', 'Is a nurse or doctor'), ('billing', 'Is at the billing desk')),
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(choices=[('A', 'Hematologic Laboratory'), ('B', 'Red blood cell '), ('C', 'White blood cell'), ('D', 'Liver function test'), ('E', 'Renal function test'), ('F', 'Electrolyte test'), ('G', 'Radiologic Laboratory'), ('H', 'X-ray'), ('I', 'Computed Tomography (CT)'), ('J', 'Magnetic Resonance Image (MRI)'), ('K', 'Urinary Test'), ('L', 'Stool Test')], max_length=1)),
                ('cost', models.FloatField(help_text='Weight in kg: ', validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(choices=[('A', 'Insulin'), ('B', 'Candesartan'), ('C', 'Dexamethasone'), ('D', 'Azithromycin'), ('E', 'Fluticasone'), ('F', 'Alteplase'), ('G', 'Aspirin')], max_length=1)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnose', models.CharField(choices=[('A', 'Diabetes'), ('B', 'Hypertension'), ('C', 'Covid'), ('D', 'Pneumonia'), ('E', 'Asthma'), ('F', 'Stroke'), ('G', 'Heart attack')], max_length=1)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
        migrations.CreateModel(
            name='CovidVaccineInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booster_shot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='booster', to='staff.covidvaccineshot')),
                ('first_shot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shot1', to='staff.covidvaccineshot')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
                ('second_shot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shot2', to='staff.covidvaccineshot')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_due', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
    ]
