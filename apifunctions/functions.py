import requests
from requests.auth import HTTPBasicAuth
import json


def makeDeleteRequest(url=None, params=None, authUser='', authPass=''):
    if not url:
        return None

    headers = {'content-type': 'application/json; charset=utf-8'}

    try:
        response = requests.delete(
            url,
            params=params,
            auth=HTTPBasicAuth(authUser, authPass),
            headers=headers
        )
    except Exception as exception:
        raise exception

    return response


def makeGetRequest(url=None, params=None, authUser='', authPass=''):
    if not url:
        return None

    headers = {'content-type': 'application/json; charset=utf-8'}

    try:
        response = requests.get(
            url,
            params=params,
            auth=HTTPBasicAuth(authUser, authPass),
            headers=headers
        )
    except Exception as exception:
        raise exception

    return response


def makePatchRequest(url=None, body=None, authUser='', authPass=''):
    if not url or not body:
        return None

    jsondata = json.dumps(body)
    jsonDataBytes = jsondata.encode('utf-8')

    headers = {'content-type': 'application/json; charset=utf-8', 'content-length': str(len(jsonDataBytes))}

    try:
        response = requests.patch(
            url,
            jsonDataBytes,
            auth=HTTPBasicAuth(authUser, authPass),
            headers=headers
        )
    except Exception as exception:
        raise exception

    return response


def makePostRequest(url=None, body=None, authUser='', authPass=''):
    if not url or not body:
        return None

    jsondata = json.dumps(body)
    jsonDataBytes = jsondata.encode('utf-8')

    headers = {'content-type': 'application/json; charset=utf-8', 'content-length': str(len(jsonDataBytes))}

    try:
        response = requests.post(
            url,
            jsonDataBytes,
            auth=HTTPBasicAuth(authUser, authPass),
            headers=headers
        )
    except Exception as exception:
        raise exception

    return response


def makePutRequest(url=None, body=None, authUser='', authPass=''):
    if not url or not body:
        return None

    jsondata = json.dumps(body)
    jsonDataBytes = jsondata.encode('utf-8')

    headers = {'content-type': 'application/json; charset=utf-8', 'content-length': str(len(jsonDataBytes))}

    try:
        response = requests.put(
            url,
            jsonDataBytes,
            auth=HTTPBasicAuth(authUser, authPass),
            headers=headers
        )
    except Exception as exception:
        raise exception

    return response


def makeSoapRequest(url=None, soapAction=None, soapEnvelopeXmlNs=None, soapEnvelopeBody=None, authUser='', authPass=''):
    if not url or not soapAction:
        return None

    headers = {'content-type': 'text/xml', 'soapAction': soapAction}

    body = """
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="%s">
            <soapenv:Header/>
            <soapenv:Body>
                %s
            </soapenv:Body>
        </soapenv:Envelope>
    """ % (soapEnvelopeXmlNs, soapEnvelopeBody)

    try:
        response = requests.post(
            url,
            data=body,
            auth=HTTPBasicAuth(authUser, authPass),
            headers=headers
        )
    except Exception as exception:
        raise exception

    return response
