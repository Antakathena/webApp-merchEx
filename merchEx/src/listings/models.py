from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
...

class Band(models.Model):

    class Genre(models.TextChoices):
        ALTERNATIVE_ROCK = 'AR'
        ALTERNATIVE_METAL = "AML"
        FOLK = "F"
        INDIE_ROCK = "IR"
        POP_ROCK = "PR"


    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    # TextChoices ou types énumératifs https://docs.djangoproject.com/fr/4.0/ref/models/fields/
    biography = models.fields.TextField()
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name

