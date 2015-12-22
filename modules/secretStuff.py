"""Get the token key from json file."""
import json
import urllib

response = urllib.urlopen("https://api.myjson.com/bins/2ofe5")
getJson = json.load(response)

def getApiJson():
    apiToken = ''
    for key in getJson:
        apiToken = key['api']
    return apiToken
