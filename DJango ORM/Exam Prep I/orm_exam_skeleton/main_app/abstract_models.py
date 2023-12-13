from django.db import models
from django.core import validators


class Person(models.Model):
    full_name = models.CharField(max_length=120, validators=[validators.MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default="Unknown")

    class Meta:
        abstract = True
