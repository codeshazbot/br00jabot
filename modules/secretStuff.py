"""Get the token key from json file."""
import json
import urllib

response = urllib.urlopen("https://api.myjson.com/bins/2ofe5")
getJson = json.load(response)

def getApiJson():
    apiToken = []
    tokenQuickFix = ''
    for key in getJson:
        apiToken.append(key['api'])
    tokenQuickFix = apiToken
    return tokenQuickFix
