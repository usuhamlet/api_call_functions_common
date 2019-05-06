import requests
from requests.auth import HTTPBasicAuth
import json


def makePostRequest(url=None, body=None, authUser='', authPass=''):
    if not url or not body:
        return None

    jsondata = json.dumps(body)
    jsonDataBytes = jsondata.encode('utf-8')

    headers = {'content-type': 'application/json; charset=utf-8', 'content-length': str(len(jsonDataBytes))}
    response = requests.post(
        url,
        jsonDataBytes,
        auth=HTTPBasicAuth(authUser, authPass),
        headers=headers
    )

    return response


def makePatchRequest(url=None, body=None, authUser='', authPass=''):
    if not url or not body:
        return None

    jsondata = json.dumps(body)
    jsonDataBytes = jsondata.encode('utf-8')

    headers = {'content-type': 'application/json; charset=utf-8', 'content-length': str(len(jsonDataBytes))}
    response = requests.patch(
        url,
        jsonDataBytes,
        auth=HTTPBasicAuth(authUser, authPass),
        headers=headers
    )

    return response


def makeRequest(url=None, params=None, authUser='', authPass=''):
    if not url:
        return None

    headers = {'content-type': 'application/json; charset=utf-8'}
    response = requests.get(
        url,
        params=params,
        auth=HTTPBasicAuth(authUser, authPass),
        headers=headers
    )

    return response
