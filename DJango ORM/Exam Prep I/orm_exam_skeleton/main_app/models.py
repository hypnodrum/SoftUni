from django.db import models
from django.core import validators
from main_app.abstract_models import Person
from main_app.custom_managers import DirectorManager


class Director(Person):
    years_of_experience = models.SmallIntegerField(validators=[validators.MinValueValidator(0)], default = 0)
    objects = DirectorManager()

    def __str__(self):
        return f"Director: {self.full_name}"


class Actor(Person):
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Actor: {self.full_name}"


class Movie(models.Model):
    GENRE_CHOICES = (
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('OTHER', 'Other')
    )
    title = models.CharField(max_length=150, validators=[validators.MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES, default='Other')
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[validators.MinValueValidator(0),validators.MaxValueValidator(10)],
        default=0.0
    )
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    starring_actor = models.ForeignKey(Actor, blank=True, null=True, on_delete=models.SET_NULL, related_name='movies')
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f"Movie: {self.title}"
