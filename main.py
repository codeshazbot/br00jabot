import StringIO
import json
import logging
import random
import urllib
import urllib2
from random import randint #Dice
# for sending images
from PIL import Image
import multipart

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

TOKEN = '<API_TOKEN_HERE>'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'

VERSION = 'La version de este bot es: 0.420'

# ================================
#Emoji codes here
hot = u'\U0001F525'
grin = u'\U0001F601'
# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        if not text:
            logging.info('no text')
            return

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.encode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)

        # THE ACTUAL USER INPUT/COMMANDS START HERE
        if text.startswith('/'):
            if text == '/start' or text == '/start@Br00jaBot':
                reply('Hola, quizas debas utilizar /help para conocer mas sobre los comandos.')
                setEnabled(chat_id, True)

            elif text == '/stop' or text == '/stop@Br00jaBot':
                reply('Oww :(')
                setEnabled(chat_id, False)

            elif text == '/image' or text == '/image@Br00jaBot':
                img = Image.new('RGB', (512, 512))
                base = random.randint(0, 16777216)
                pixels = [base+i*j for i in range(512) for j in range(512)]
                # generate sample image
                img.putdata(pixels)
                output = StringIO.StringIO()
                img.save(output, 'JPEG')
                reply(img=output.getvalue())

            elif text == '/quelacreo' or text == '/quelacreo@Br00jaBot':
                #reply(VERSION) #Fixd
                reply(''.format())#wat

            #elif text == '/dado' or text == '/dado@Br00jaBot': #Dice fix'd
            #    numero = randint(0,99)
            #    resultado = ('Sacaste: ' + str(numero))
            #    reply(resultado)
        elif re.search('[/]dado', text, re.IGNORECASE):
                numero = randint(0,99)
                resultado = ('Sacaste: ' + str(numero))
                reply(resultado)

            elif text == '/changelog' or text == '/changelog@Br00jaBot':
                reply('Siempre puedes echar un vistazo en https://github.com/codeshazbot/TelegramBots para fijarte que hay de nuevo' + grin)

            elif text == '/help' or text == '/quelacreo@Br00jaBot':
                reply ('Buena nueva! Movimos el culo y colocamos cosas en este comando \n1-/quelacreo Muestra la version del bot\n2-/stop Detiene las funciones del bot\n3-/gym Muestra una pasta (Por ahora:DDDD)\n4-/dado Tira los dados, obtendras un numero entre 1 y 99\n5-/changelog Te dira que funciones hemos estado agregando tras cada update\n\nY... Eso es todo.')

            elif text == '/gym' or text == '/gym@Br00jaBot': #Eliminada la reply que decia 'pasta incoming'
                reply('ah pues maldito maricon, debes saber que yo fui al gym maldito comemierda y me la pasaba echandole maltas a los culos de las carajas que estaban ahi mientras me las pegaba y levantaba pesas, tambien se lo mamaba a los otros carajos que estaban ahi que se ponian todos maricos a decirme "ay papi tu si tas bueno" yo les decia "ay vale, maldito maricon de mierda, tu lo que quieres es que te mame el guevo verdad, muchacho marico pelate esa vaina" y se la pelaba y yo le daba, asi que no creas que me voy a cortar contigo maldito marico, que te tengo fichado bruja, becerro, cdtm sapo diablon, MAMAGUEVO, debes saber que de carajito me quedaba con mi mama a amarrar hallacas en la casa asi que se todo sobre defenderme muchacho marico, asi que abre canchas pues, tu crees que me arde el culo? no papa, yo soy experto en aguantar ardor de culo, ya que me meto los dildos de mi mama para estimular mi prostata, tambien lo hago en el gym y las tipas les gusta, asi que habla claro becerro.  Tu quieres que yo te lo mame o que?')

            else:
                reply('Soy marico y me meto comandos por el culo, lo lamento, ese tambien me lo meti') #Fix'dx2

        # CUSTOM MESSAGES AND FALLBACK ERROR MESSAGES

        elif 'no leer' in text: #Erased "else" in order to prevent reply loop
            reply('Los creadores de este bot claramente no saben que es leer')


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
