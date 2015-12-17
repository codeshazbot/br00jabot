"""This add epic pastas."""

import random
import json
import urllib

# load epic pasta from json file
url = 'https://api.myjson.com/bins/4uxpd'
response = urllib.urlopen(url)
jsonMeme = json.load(response)


def getPasta():
    """Get the pastallioni."""
    pastas = []
    for meme in jsonMeme:
        pastas.append(meme['epicPasta'])
    return random.choice(pastas)
