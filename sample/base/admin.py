from django.contrib import admin

# Register your models here.
from sample.base import models


@admin.register(models.FoursquareVenue)
class FoursquareVenueAdmin(admin.ModelAdmin):
    """
    FoursquareVenue Admin
    """
    list_display = ['name', 'address', 'venue_id', 'visited', 'request_id']
    search_fields = ['name', 'address']