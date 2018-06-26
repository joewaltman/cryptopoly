from rest_framework import serializers

from sample.base.models import FoursquareVenue


class FoursquareVenueSerializer(serializers.ModelSerializer):
    """
    FoursquareVenue Serializer
    """

    class Meta:
        """
        FoursquareVenue Meta
        """
        model = FoursquareVenue
        fields = '__all__'

    def update(self, instance, validated_data):
        print("inside update")
        instance.visited += 1
        instance.save()
        return instance
