from django.db import models

# Create your models here.
from django.db.models import CharField, DecimalField, TextField, PositiveIntegerField
from djutil.models import TimeStampedModel


class FoursquareVenue(TimeStampedModel):
    """
    Assignment model
    """
    venue_id = CharField(max_length=50, unique=True)
    name = CharField(max_length=200, null=True, blank=True)
    latitude = DecimalField(max_digits=30, decimal_places=20)
    longitude = DecimalField(max_digits=30, decimal_places=20)
    address = TextField(null=True, blank=True)
    visited = PositiveIntegerField(default=1)
    request_id = CharField(max_length=50)

    def __str__(self):
        return self.name
