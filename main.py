from telegram import Updater
updater = Updater(token='<API_TOKEN_HERE>')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Soy es lacra, llegate")


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Soy marico y me meto comandos por el culo, lo siento, ese tambien me lo meti")


def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="lolnada")

dispatcher.addUnknownTelegramCommandHandler(unknown)
dispatcher.addTelegramMessageHandler(echo)
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('help', help)
updater.start_polling()
