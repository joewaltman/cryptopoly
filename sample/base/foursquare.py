import json

import requests

from sample import settings

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
    data = json.loads(resp.text)
    data = data["response"]["groups"][0]["items"]
    return data
