import praw
import random


# Muh shitty def
def getRandomPic():
    temp = []
    randomPic = random.randrange(0, 24)
    r = praw.Reddit('Random Picture Grab')
    for submission in r.get_subreddit('lolcats').get_new(limit=25):
        temp.append(submission.url)
    return temp[randomPic]

# TODO: El Bot necesita una imagen(.jpg .png) para
# enviarla en el chat no una URL de la imagen.
# Buscar la forma cargar y guardar la imagen desde la URL.
