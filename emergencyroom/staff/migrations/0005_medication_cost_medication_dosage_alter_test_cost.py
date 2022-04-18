# Generated by Django 4.0.4 on 2022-04-12 04:51

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_medication_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='cost',
            field=models.FloatField(default=100, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medication',
            name='dosage',
            field=models.FloatField(default=0.5, help_text='Dosage in mg', validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='cost',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
