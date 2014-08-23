import requests

from requests.exceptions import HTTPError
from time import sleep

from django.conf import settings


BASE_API_URL = 'https://na.api.pvp.net/api/lol/{region}/{version}/{endpoint}'


def make_request(endpoint, version, region, api_key=settings.LOL_API_KEY, sleep_time=None):
    try:
        full_url = BASE_API_URL.format(region=region, version=version, endpoint=endpoint)

        r = requests.get(full_url, params={'api_key': api_key})

        if sleep_time:
            sleep(sleep_time)

        return r.json()

    except HTTPError, e:
        # TODO: Figure out logging
        print e

        if sleep_time:
            sleep(sleep_time)

        raise e
