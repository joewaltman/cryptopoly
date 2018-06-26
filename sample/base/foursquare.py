import json

import requests

from sample import settings
from sample.base.models import FoursquareVenue
from sample.base.serializers.venue import FoursquareVenueSerializer

url = 'https://api.foursquare.com/v2/venues/explore'


def make_foursquare_call(lat, lng, query, limit=10):
    lat_lng = ",".join([lat, lng])
    params = dict(
        client_id=settings.FOURSQUARE_CLIENT_ID,
        client_secret=settings.FOURSQUARE_CLIENT_SECRET,
        v='20180323',
        ll=lat_lng,
        query=query,
        limit=limit
    )
    resp = requests.get(url=url, params=params)
    print(resp.text)
    data = json.loads(resp.text)
    data["venues"] = data["response"]["groups"][0]["items"]
    data["request_id"] = data["meta"]["requestId"]
    return data


def update_foursquare_data(data):
    """
    Update foursqaure venue table from data
    :param data:
    :return:
    """
    if data:
        for obj in data["venues"]:
            venue = obj["venue"]
            venue_data = dict()
            venue_data["venue_id"] = venue["id"]
            venue_data["name"] = venue["name"]
            venue_data["address"] = venue["location"].get("address")
            venue_data["latitude"] = venue["location"]["lat"]
            venue_data["longitude"] = venue["location"]["lng"]
            venue_data["request_id"] = data["request_id"]
            venue_serializer = FoursquareVenueSerializer(data=venue_data, instance=get_venue_by_id(venue["id"]))
            if venue_serializer.is_valid():
                venue_serializer.save()
            else:
                print(venue_serializer.errors)


def get_venue_by_id(venue_id):
    """
    Get Venye by foursquare id
    :param venue_id:
    :return:
    """
    try:
        return FoursquareVenue.objects.get(venue_id=venue_id)
    except FoursquareVenue.DoesNotExist as exc:
        return None


def get_related_venues(request_id):
    """
    Get related venues by grouping them with request id
    :param request_id:
    :return:
    """
    venues = FoursquareVenue.objects.filter(request_id=request_id)
    venues_data = FoursquareVenueSerializer(instance=venues, many=True)
    return venues_data.data