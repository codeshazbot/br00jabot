"""This add epic pastas."""

import random
import json

# load epic pasta from json file
jsonMeme = json.loads(open('../memes.json').read())


def getPasta():
    """Get the pastallioni."""
    pastas = []
    for meme in jsonMeme:
        pastas.append(meme['epicPasta'])
    return random.choice(pastas)
