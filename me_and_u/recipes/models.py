""" Model(s) used in recipe operations.
"""

from django.db import models
from tinymce.models import HTMLField
from me_and_u.core.models import UUIDTimeStampedModel

class Recipe(UUIDTimeStampedModel):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    ingredients = HTMLField()
    steps = HTMLField()
    notes = HTMLField(blank=True)

    def __str__(self):
        return self.name
