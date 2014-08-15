import requests
from requests.exceptions import HTTPError

from django.conf import settings


BASE_API_URL = 'https://na.api.pvp.net/api/lol/{region}/{version}/{endpoint}'


def make_request(endpoint, version, region='na', api_key=settings.LOL_API_KEY):
    try:
        full_url = BASE_API_URL.format(region=region, version=version, endpoint=endpoint)
        r = requests.get(full_url, params={'api_key': api_key})
        return r.json()

    except HTTPError, e:
        print e
        raise e
