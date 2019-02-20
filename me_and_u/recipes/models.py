""" Model(s) used in recipe operations.
"""

from django.db import models
from me_and_u.core.models import TimeStampedModel

class Recipe(TimeStampedModel):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ingredients = models.TextField()
    steps = models.TextField()

    def __str__(self):
        return self.name
