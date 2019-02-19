""" Models to be inherited from across other apps
"""

from django.db import models

class TimeStampedModel(models.Model):
    """ An abstract base class model that provides self-updating `created` and `modified` fields.
        Super Duper stolen from Two Scoops of Django 1.11
            6.1.3 Model Inheritance in Practice: The TimeStampedModel
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
