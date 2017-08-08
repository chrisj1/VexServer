import json
import requests


def get_json_from_URL(url):
    r = requests.get(url)

    return r.json()