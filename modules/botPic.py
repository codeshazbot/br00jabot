import praw
import random


# Muh shitty def
def getRandomPic():
    temp = []
    r = praw.Reddit('Random Picture Grab')
    for submission in r.get_subreddit('lolcats').get_new(limit=25):
        temp.append(submission.url)
    return random.choice(temp)
    
# bot loads a link and telegram takes care of loading the preview so it's fine
