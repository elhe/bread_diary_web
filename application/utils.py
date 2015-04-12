import json

import requests


__author__ = 'elhe'


def send_json_request(method, url, data):
    app_url = 'http://localhost:5000'  # TODO
    full_url = '%s%s' % (app_url, url)
    return requests.request(method, full_url,
                            headers={'content-type': 'application/json'}, data=json.dumps(data))