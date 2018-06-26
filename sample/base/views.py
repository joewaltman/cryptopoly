"""
Base View Files
"""

from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.views import APIView

from sample.base.foursquare import make_foursquare_call, update_foursquare_data, get_venue_by_id, get_related_venues
from sample.base.serializers.venue import FoursquareVenueSerializer


class Index(APIView):
    """
    Home Page
    """
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request):
        """
        edit an assignment
        """
        return Response(template_name='index.html')


class GetFourSquareData(APIView):
    """
    Get foursquare data
    """
    renderer_classes = (renderers.JSONRenderer,)

    def get(self, request):
        """
        Get foursquare data
        """

        lat = request.GET.get("lat")
        lng = request.GET.get("lng")
        query = request.GET.get("query", "")
        if not lat or not lng:
            return Response({"error": "Please provide sufficient data"})
        data = make_foursquare_call(lat, lng, query)
        update_foursquare_data(data)
        return Response({"data": data})


class Buy(APIView):
    """
    Buy from foursquare data
    """
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request):
        """
        Get foursquare data
        """

        venue_id = request.GET.get("venue")
        venue = FoursquareVenueSerializer(instance=get_venue_by_id(venue_id)).data
        related_venues = get_related_venues(venue["request_id"])
        return Response({"venue": venue, "related_venues": related_venues}, template_name='buy.html')
