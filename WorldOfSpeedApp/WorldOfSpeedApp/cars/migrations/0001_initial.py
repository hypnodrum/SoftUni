# Generated by Django 4.2.10 on 2024-02-24 09:11

import WorldOfSpeedApp.cars.custom_validators
import WorldOfSpeedApp.cars.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('Rally', 'Rally'), ('Open-wheel', 'Open-wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10)),
                ('car_model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1)])),
                ('year', models.IntegerField(validators=[WorldOfSpeedApp.cars.custom_validators.car_year_validator])),
                ('image_url', WorldOfSpeedApp.cars.models.UniqueURLField(unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='profiles.profile')),
            ],
        ),
    ]
