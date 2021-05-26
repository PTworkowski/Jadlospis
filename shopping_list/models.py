from django.db import models

# Create your models here.
from django.conf import settings


class Ingredient(models.Model):
    KILOGRAM = 'kg'
    GRAM = 'g'
    PIECES = 'szt'
    UNIT_CHOICES = [
        (KILOGRAM, 'Kilo'),
        (GRAM, 'Gram'),
        (PIECES, 'Sztuk'),
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=250, primary_key=True, unique=True)
    package_size = models.IntegerField(default=1)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default=PIECES)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
