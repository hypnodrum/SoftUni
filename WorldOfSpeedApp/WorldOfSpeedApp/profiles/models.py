from django.core.validators import MinValueValidator
from django.db import models
from WorldOfSpeedApp.profiles.custom_validators import user_name_validator, custom_minlength_validator


class Profile (models.Model):

    username = models.CharField(
        max_length=15,
        validators=(custom_minlength_validator, user_name_validator,),
        blank=False,
        null=False
    )
    email = models.EmailField(blank=False, null=False)
    age = models.IntegerField(
        validators=(MinValueValidator(21),),
        help_text="Age requirement: 21 years and above."
    )
    password = models.CharField(max_length=20, blank=False, null=False)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
