import urllib

def query_api(mode='viewstatus'):
    url = "https://devlol.org/status/hackerspaceapi/"
    return urllib.urlopen(url + mode).read()

def get():
    try:
        return 'OPEN' in query_api()
    except:
        return None
