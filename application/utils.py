import json

import requests


__author__ = 'elhe'
APP_URL = 'http://localhost:5000'  # TODO


def send_http_request(method, url, **kwargs):
    full_url = '%s%s' % (APP_URL, url)
    return requests.request(method, full_url, **kwargs)


def send_json_request(method, url, data):
    full_url = '%s%s' % (APP_URL, url)
    return requests.request(method, full_url,
                            headers={'content-type': 'application/json'}, data=json.dumps(data))