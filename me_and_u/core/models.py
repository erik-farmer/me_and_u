""" Models to be inherited from across other apps
"""
import uuid
from django.db import models

class UUIDTimeStampedModel(models.Model):
    """ An abstract base class model that provides self-updating `created` and `modified` fields.
        Also includes public id field for exposing references (e.g. urls)
        Super Duper stolen from Two Scoops of Django 1.11
            6.1.3 Model Inheritance in Practice: The TimeStampedModel
    """
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
