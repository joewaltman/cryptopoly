"""
Base View Files
"""

from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.views import APIView

from sample.base.foursquare import make_foursquare_call


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
        return Response({"data": data})
