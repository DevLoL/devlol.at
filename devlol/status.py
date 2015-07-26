import urllib
import json

def query_api(mode='viewstatus'):
    url = "https://devlol.org/status/hackerspaceapi/"
    return urllib.urlopen(url + mode).read()

def isLocked():
    try:
        data = json.loads(query_api(mode=''))
        return bool(data['sensors']['door_locked'][0]['value'])
    except:
        return None

def isOpen():
    return not isLocked()
